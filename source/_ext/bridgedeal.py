"""A boxed West/East deal for the repeated example called The Hand.

Suits stay ordinary Unicode text, the same symbols the rest of the book
uses. No color is applied. HTML and EPUB get a bordered table; LaTeX gets
a bordered tabular; the text builder gets an ASCII box.
"""

from html import escape

from docutils import nodes
from docutils.parsers.rst import Directive

SUITS = ("♠", "♥", "♦", "♣")
SEATS = ("West", "East")


class bridge_deal(nodes.General, nodes.Element):
    pass


def _parse_line(line):
    text = line.strip()
    seat = next((name for name in SEATS if text.startswith(name)), None)
    if seat is None:
        raise ValueError("each line must start with West or East")
    rest = text[len(seat):].strip()
    marks = []
    for suit in SUITS:
        at = rest.find(suit)
        if at < 0:
            raise ValueError("missing %s" % suit)
        marks.append((at, suit))
    marks.sort()
    cards = {}
    for index, (at, suit) in enumerate(marks):
        end = marks[index + 1][0] if index + 1 < len(marks) else len(rest)
        cards[suit] = rest[at + len(suit):end].strip()
    return seat, cards


def _columns(node):
    return [seat for seat in SEATS if seat in node["hands"]]


def _cell(hand, suit):
    # One space after the symbol; ranks stay run together (K862).
    return "%s %s" % (suit, hand[suit])


class BridgeDealDirective(Directive):
    has_content = True

    def run(self):
        hands = {}
        try:
            for line in self.content:
                if not line.strip():
                    continue
                seat, cards = _parse_line(line)
                if seat in hands:
                    raise ValueError("%s is given twice" % seat)
                hands[seat] = cards
            if not hands:
                raise ValueError("no hands given")
        except ValueError as exc:
            message = "bridge-deal: %s" % exc
            error = self.state.document.reporter.error(
                message,
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
            )
            return [error]
        node = bridge_deal()
        node["hands"] = hands
        return [node]


def _html_table(node):
    columns = _columns(node)
    border = "2px solid #000"

    def edges(col, top, bottom):
        bits = [
            "border-top:%s" % (border if top else "none"),
            "border-bottom:%s" % (border if bottom else "none"),
            "border-left:%s" % (border if col == 0 else "none"),
            "border-right:%s" % border,
            "padding:0.15em 1.15em",
            "color:#000",
            "background:#fff",
        ]
        return ";".join(bits)

    head = []
    for col, seat in enumerate(columns):
        style = edges(col, True, True) + ";text-align:center;font-weight:bold;padding:0.4em 1.15em"
        head.append("<th style=\"%s\">%s</th>" % (style, escape(seat)))
    body = []
    for row, suit in enumerate(SUITS):
        last = row == len(SUITS) - 1
        cells = []
        for col, seat in enumerate(columns):
            style = edges(col, False, last) + ";text-align:left;font-weight:normal"
            cells.append("<td style=\"%s\">%s</td>" % (style, escape(_cell(node["hands"][seat], suit))))
        body.append("<tr>%s</tr>" % "".join(cells))
    return (
        "<table class=\"bridge-deal\" style=\"border-collapse:collapse;border-spacing:0;"
        "margin:0.8em 0 1em 0;width:auto;background:#fff;color:#000\">"
        "<thead><tr>%s</tr></thead><tbody>%s</tbody></table>"
        % ("".join(head), "".join(body))
    )


def visit_html(self, node):
    self.body.append(_html_table(node))
    raise nodes.SkipNode


def _latex_escape(text):
    return (
        text.replace("\\", r"\textbackslash{}")
        .replace("&", r"\&")
        .replace("%", r"\%")
        .replace("$", r"\$")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("{", r"\{")
        .replace("}", r"\}")
    )


def visit_latex(self, node):
    columns = _columns(node)
    spec = "|".join(["l"] * len(columns))
    lines = [
        r"{\setlength{\arrayrulewidth}{0.8pt}",
        r"\begin{tabular}{|%s|}" % spec,
        r"\hline",
    ]
    # The first cell draws the shared vertical rule. Later cells draw only
    # their right edge, so the divider is a single line.
    header_cells = []
    for index, seat in enumerate(columns):
        if len(columns) == 1:
            edge = "|c|"
        elif index == 0:
            edge = "|c|"
        else:
            edge = "c|"
        header_cells.append(r"\multicolumn{1}{%s}{\textbf{%s}}" % (edge, _latex_escape(seat)))
    lines.append(" & ".join(header_cells) + r" \\")
    lines.append(r"\hline")
    for suit in SUITS:
        row = " & ".join(
            _latex_escape(_cell(node["hands"][seat], suit)) for seat in columns
        )
        lines.append(row + r" \\")
    lines.append(r"\hline")
    lines.append(r"\end{tabular}}")
    lines.append("")
    self.body.append("\n" + "\n".join(lines))
    raise nodes.SkipNode


def visit_text(self, node):
    columns = _columns(node)
    rows = [[seat for seat in columns]]
    for suit in SUITS:
        rows.append([_cell(node["hands"][seat], suit) for seat in columns])
    widths = [max(len(row[col]) for row in rows) for col in range(len(columns))]
    rule = "+" + "+".join("-" * (width + 2) for width in widths) + "+"

    def format_row(cells):
        return "|" + "|".join(" " + cell.ljust(widths[i]) + " " for i, cell in enumerate(cells)) + "|"

    block = [rule, format_row(rows[0]), rule]
    for cells in rows[1:]:
        block.append(format_row(cells))
    block.append(rule)
    self.new_state(0)
    self.add_text("\n".join(block))
    self.end_state(wrap=False)
    raise nodes.SkipNode


def setup(app):
    app.add_directive("bridge-deal", BridgeDealDirective)
    app.add_node(
        bridge_deal,
        html=(visit_html, None),
        latex=(visit_latex, None),
        text=(visit_text, None),
    )
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
