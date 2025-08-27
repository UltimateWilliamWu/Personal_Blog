# EDIT THE FILE WITH YOUR SOLUTION
import re
from fractions import Fraction
import math

base_shapes = {
    "Large triangle": {
        0: [("0", "0"), ("2", "2"), ("2", "0")],
        45: [("0", "0"), ("0", "2*sqrt(2)"), ("sqrt(2)", "sqrt(2)")]
    },
    "Small triangle": {
        0: [("0", "0"), ("1", "1"), ("1", "0")],
        45: [("0", "0"), ("0", "sqrt(2)"), ("0.5*sqrt(2)", "0.5*sqrt(2)")]
    },
    "Medium triangle": {
        0: [("0", "0"), ("1", "1"), ("2", "0")],
        45: [("0", "0"), ("0", "sqrt(2)"), ("sqrt(2)", "sqrt(2)")]
    },
    "Square": {
        0: [("0", "0"), ("0", "1"), ("1", "1"), ("1", "0")],
        45: [("0", "0"), ("-0.5*sqrt(2)", "0.5*sqrt(2)"), ("0", "sqrt(2)"), ("0.5*sqrt(2)", "0.5*sqrt(2)")]
    },
    "Parallelogram": {
        0: [("0", "0"), ("1", "1"), ("2", "1"), ("1", "0")],
        45: [("0", "0"), ("0", "sqrt(2)"), ("0.5*sqrt(2)", "1.5*sqrt(2)"), ("0.5*sqrt(2)", "0.5*sqrt(2)")]
    },
}


def _parse_expr(expr):
    tokens = expr.replace(" ", "").replace("-", " -").replace("+", " +").split()
    rational = Fraction(0)
    sqrt_coeff = Fraction(0)
    for token in tokens:
        if "sqrt(2)" not in token:
            rational += Fraction(token)
        else:
            coeff = token.replace("sqrt(2)", "").replace("*", "")
            if coeff == "" or coeff == "+":
                sqrt_coeff += 1
            elif coeff == "-":
                sqrt_coeff -= 1
            else:
                sqrt_coeff += Fraction(coeff)
    return rational, sqrt_coeff


def _format(base, root):
    global root_part
    parts = []
    if base != 0:
        parts.append(str(base))
    if root != 0:
        is_negative = root < 0
        if base != 0:
            root = abs(root)
        if root.denominator != 1:
            root_part = f"({root})√2"
        elif root.numerator != 1 and root.numerator != -1:
            root_part = f"{root}√2"
        elif root.numerator == 1:
            root_part = "√2"
        elif root.numerator == -1:
            root_part = "-√2"

        if base == 0:
            parts.append(root_part)
        else:
            parts.append(f"- {root_part}" if is_negative else f"+ {root_part}")
    return " ".join(parts) if parts else "0"


def _format_tex(rational, sqrt):
    result = ""
    if rational != 0:
        result += str(rational)
    if sqrt != 0:
        if sqrt > 0 and rational != 0:
            result += "+"
        elif sqrt < 0:
            result += "-"

        coeff = abs(sqrt)
        if coeff == 1:
            result += "sqrt(2)"
        else:
            result += f"{coeff}*sqrt(2)"
    if not result:
        return "0"
    return result


class Point:
    def __init__(self, x_expr, y_expr):
        self.x_base, self.x_root = _parse_expr(x_expr)
        self.y_base, self.y_root = _parse_expr(y_expr)

    def __str__(self):
        return f"({_format(self.x_base, self.x_root)}, {_format(self.y_base, self.y_root)})"

    def rotate_90(self):
        new_x_base = -self.y_base
        new_x_root = -self.y_root
        new_y_base = self.x_base
        new_y_root = self.x_root

        self.x_base, self.x_root = new_x_base, new_x_root
        self.y_base, self.y_root = new_y_base, new_y_root

    def flip(self, flip_x=False, flip_y=False):
        if flip_x:
            self.x_base, self.x_root = -self.x_base, -self.x_root
        if flip_y:
            self.y_base, self.y_root = -self.y_base, -self.y_root

    def move(self, anchor):
        self.x_base += anchor.x_base
        self.x_root += anchor.x_root
        self.y_base += anchor.y_base
        self.y_root += anchor.y_root

    def approx_x(self):
        return float(self.x_base) + float(self.x_root) * 2 ** 0.5

    def approx_y(self):
        return float(self.y_base) + float(self.y_root) * 2 ** 0.5

    def __eq__(self, other):
        return self.x_root == other.x_root and self.x_base == other.x_base and self.y_root == other.y_root and self.y_base == other.y_base


def decode_options(options):
    flip_x, flip_y, angle = False, False, 0
    for option in options:
        name, value = option.split("=")
        if name == "xscale" and value == "-1":
            flip_x = True
        if name == "yscale" and value == "-1":
            flip_y = True
        if name == "rotate":
            angle = int(value)
    if flip_x and flip_y:
        angle += 180
        flip_x, flip_y = False, False
    return flip_x, flip_y, angle % 360


def remove_opposite(edges):
    result = []
    for e1 in edges:
        canceled = False
        for e2 in edges:
            if e1.start == e2.end and e1.end == e2.start:
                canceled = True
        if not canceled:
            result.append(e1)
    return result

# def remove_opposite(edges):
#     seen = set()
#     result = []
#
#     for edge in edges:
#         key = (str(edge.start), str(edge.end))
#         reverse_key = (str(edge.end), str(edge.start))
#
#         if reverse_key in seen:
#             seen.remove(reverse_key)  # 删除匹配的反向边
#             continue
#         seen.add(key)
#         result.append(edge)
#
#     return result


def merge_edges(edges):
    changed = True
    while changed:
        changed = False
        new_edges = []
        used = set()

        for e1 in edges:
            if e1 in used:
                continue
            merged = False
            for e2 in edges:
                if e2 in used or e1 is e2:
                    continue
                if (e1.end == e2.start or e2.end == e1.start) and e1.compare_direction_with(e2) == 1:
                    if e1.end == e2.start:
                        new_edge = Edge(e1.start, e2.end)
                    else:
                        new_edge = Edge(e2.start, e1.end)
                    new_edges.append(new_edge)
                    used.add(e1)
                    used.add(e2)
                    changed = True
                    merged = True
                    break
            if not merged:
                new_edges.append(e1)
                used.add(e1)
        edges = new_edges
    return edges


def merge_opposite(edges):
    result = []
    used = set()
    for e1 in edges:
        if e1 in used:
            continue
        merged = False

        for e2 in edges:
            if e2 in used or e1 is e2:
                continue
            if e1.compare_direction_with(e2) != -1:
                continue
            points = [e1.start, e1.end, e2.start, e2.end]
            points.sort(key=lambda p: (p.approx_x(), p.approx_y()))
            p0, p1, p2, p3 = points

            if ((p0 == e1.start and p1 == e1.end) or (p0 == e1.end and p1 == e1.start) or (
                    p0 == e2.start and p1 == e2.end) or (
                    p0 == e2.end and p1 == e2.start)):
                continue
            used.add(e1)
            used.add(e2)
            merged = True
            if e1.start != e2.end:
                result.append(Edge(e1.start, e2.end))
            if e2.start != e1.end:
                result.append(Edge(e2.start, e1.end))
            break

        if not merged:
            result.append(e1)
    return result


class TangramPuzzle:
    def __init__(self, filename):
        with open(filename) as file:
            self.lines = file.readlines()
        self.shapes = []
        self.transformations = self.extract_transformations()
        self.shapes.sort(key=lambda item: (-item[1][0].approx_y(), item[1][0].approx_x(), item[1][1].approx_x()))

    def extract_transformations(self):
        result = {}
        for line in self.lines:
            if "PieceTangram" not in line:
                continue
            shape_name, flip_x, flip_y, angle = self.parse_line(line)
            if shape_name in result:
                shape_name = shape_name.replace("1", "2")
            result[shape_name] = {
                "rotate": angle,
                "xflip": flip_x,
            }
        return result

    def parse_line(self, line):
        shape_mapping = {
            "TangCar": "Square",
            "TangGrandTri": "Large triangle 1",
            "TangMoyTri": "Medium triangle",
            "TangPetTri": "Small triangle 1",
            "TangPara": "Parallelogram",
        }
        shape_key = re.findall(r"\{([^{}]*)}", line)[-1]
        shape_name = shape_mapping[shape_key]
        options = re.findall(r"<([^<>]*)>", line)
        if options:
            options = options[0].replace(" ", "").split(",")
        flip_x, flip_y, angle = decode_options(options)
        anchor_coords = re.findall(r"\{([^{}]*)}", line)[:2]
        self.compute_vertices(anchor_coords, shape_name.replace(" 1", ""), flip_x, flip_y, angle)
        return shape_name, flip_x, flip_y, angle

    def compute_vertices(self, anchor_text, shape_type, flip_x, flip_y, angle):
        anchor_point = Point(anchor_text[0], anchor_text[1])
        base_angle = 0 if angle % 90 == 0 else 45
        template = base_shapes[shape_type][base_angle]
        steps = (angle - base_angle) // 90
        points = [Point(x, y) for x, y in template]
        for pt in points:
            for _ in range(steps):
                pt.rotate_90()
            pt.flip(flip_x=flip_x, flip_y=flip_y)
            pt.move(anchor_point)
        if flip_x != flip_y:
            points = points[::-1]
        top_left = min(points, key=lambda pt: (-pt.approx_y(), pt.approx_x()))
        top_index = points.index(top_left)
        points = points[top_index:] + points[:top_index]
        self.shapes.append((shape_type, points))

    def __str__(self):
        lines = []
        for shape_name, points in self.shapes:
            points_str = ", ".join(str(pt) for pt in points)
            line = f"{shape_name:15}: [{points_str}]"
            lines.append(line)
        return "\n".join(lines)

    def draw(self, file):
        all_points = []
        for shape, points in self.shapes:
            for point in points:
                all_points.append(point)
        all_x = [p.approx_x() for p in all_points]
        all_y = [p.approx_y() for p in all_points]
        x_min = math.floor(min(all_x) * 2 - 1) / 2
        x_max = math.ceil(max(all_x) * 2 + 1) / 2
        y_min = math.floor(min(all_y) * 2 - 1) / 2
        y_max = math.ceil(max(all_y) * 2 + 1) / 2
        with open(file, "w") as f:
            f.write("\\documentclass{standalone}\n")
            f.write("\\usepackage{tikz}\n")
            f.write("\\begin{document}\n\n")
            f.write("\\begin{tikzpicture}\n")
            f.write(f"\\draw[step=5mm] ({x_min}, {y_min}) grid ({x_max}, {y_max});\n")

            for _, points in self.shapes:
                coords = []
                for p in points:
                    coords.append(f"({{{_format_tex(p.x_base, p.x_root)}}}, {{{_format_tex(p.y_base, p.y_root)}}})")
                f.write(f"\\draw[ultra thick] {" -- ".join(coords)} -- cycle;\n")
            f.write("\\fill[red] (0,0) circle (3pt);\n")
            f.write("\\end{tikzpicture}\n\n")
            f.write("\\end{document}\n")

    def get_all_edge(self):
        edges = []
        for _, points in self.shapes:
            for i in range(len(points)):
                start = points[i]
                end = points[(i + 1) % len(points)]
                edge = Edge(start, end)
                edges.append(edge)
        return edges

    def trace_closed_loop_backtrack(self, edges):
        start_point = self.shapes[0][1][0]
        n = len(edges)

        def backtrack(path, remaining, cur_point):
            if not remaining:
                if cur_point == start_point:
                    return path
                return None
            candidates = [e for e in remaining if e.start == cur_point]
            for edge in candidates:
                next_point = edge.end
                next_path = path + [edge]
                next_remaining = remaining.copy()
                next_remaining.remove(edge)

                result = backtrack(next_path, next_remaining, next_point)
                if result:
                    return result
            return None

        result = backtrack([], edges.copy(), start_point)
        return result

    def draw_outline(self, file):
        all_points = [p for _, shape in self.shapes for p in shape]
        all_x = [p.approx_x() for p in all_points]
        all_y = [p.approx_y() for p in all_points]
        x_min = math.floor(min(all_x) * 2 - 1) / 2
        x_max = math.ceil(max(all_x) * 2 + 1) / 2
        y_min = math.floor(min(all_y) * 2 - 1) / 2
        y_max = math.ceil(max(all_y) * 2 + 1) / 2

        edges = self.get_all_edge()
        edges = remove_opposite(edges)
        edges = merge_edges(edges)
        edges = merge_opposite(edges)
        final_edges = self.trace_closed_loop_backtrack(edges)
        with open(file, "w") as f:
            f.write("\\documentclass{standalone}\n")
            f.write("\\usepackage{tikz}\n")
            f.write("\\begin{document}\n\n")
            f.write("\\begin{tikzpicture}\n")
            f.write(f"\\draw[step=5mm] ({x_min}, {y_min}) grid ({x_max}, {y_max});\n")
            f.write(f"\\draw[ultra thick]\n")

            for edge in final_edges:
                p = edge.start
                if edge != final_edges[-1]:
                    f.write(
                        f"    ({{{_format_tex(p.x_base, p.x_root)}}}, {{{_format_tex(p.y_base, p.y_root)}}}) --\n")
                else:
                    f.write(
                        f"    ({{{_format_tex(p.x_base, p.x_root)}}}, {{{_format_tex(p.y_base, p.y_root)}}}) -- cycle;\n")
            f.write("\\fill[red] (0,0) circle (3pt);\n")
            f.write("\\end{tikzpicture}\n\n")
            f.write("\\end{document}\n")


class Edge:
    def __init__(self, start_point, end_point):
        self.start = start_point
        self.end = end_point
        self.unit_vector = self._compute_unit_vector()

    def _compute_unit_vector(self):
        dx = self.end.approx_x() - self.start.approx_x()
        dy = self.end.approx_y() - self.start.approx_y()
        length = (dx ** 2 + dy ** 2) ** 0.5
        if length == 0:
            return 0.0, 0.0
        return dx / length, dy / length

    def compare_direction_with(self, other_edge):
        dx1, dy1 = self.unit_vector
        dx2, dy2 = other_edge.unit_vector
        dot_product = dx1 * dx2 + dy1 * dy2

        if dot_product == 1:
            direction = 1
        elif dot_product == -1:
            direction = -1
        else:
            return 0

        test_vector = Edge(self.start, other_edge.start).unit_vector
        cross_product = dx1 * test_vector[1] - dy1 * test_vector[0]
        if abs(cross_product) > 0:
            return 0
        return direction


# T = TangramPuzzle("kangaroo.tex")
# for piece in T.transformations:
#     print(f"{piece:16}: {T.transformations[piece]}")
TangramPuzzle("kangaroo.tex").draw("kangaroo_on_grid.tex")
TangramPuzzle("kangaroo.tex").draw_outline("kangaroo_outline.tex")
TangramPuzzle("cat.tex").draw("cat_on_grid.tex")
TangramPuzzle("cat.tex").draw_outline("cat_outline.tex")
TangramPuzzle("goose.tex").draw("goose_on_grid.tex")
TangramPuzzle("goose.tex").draw_outline("goose_outline.tex")
