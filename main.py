from manim import *

class FunctionGraphScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-5, 5, 1],
            x_length=7,
            y_length=6,
            axis_config={"color": BLUE},
        ).add_coordinates()

        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        graph = axes.plot(lambda x: x**2 - 4, color=YELLOW)
        func_label = MathTex(r"f(x) = x^2 - 4", color=YELLOW).next_to(axes, UP)

        self.play(Create(axes), Write(axes_labels))
        self.play(Write(func_label))
        self.play(Create(graph), run_time=2)

        dot1 = Dot(axes.c2p(-2, 0), color=RED)
        dot2 = Dot(axes.c2p(2, 0), color=RED)
        root_label = Text("Roots: x = -2, 2", font_size=24, color=RED).to_corner(UR)

        self.play(FadeIn(dot1), FadeIn(dot2), Write(root_label))

        tracker = ValueTracker(-1.5)
        tangent = always_redraw(
            lambda: axes.get_tangent_line(
                x=tracker.get_value(), graph=graph, length=4, color=GREEN
            )
        )

        self.play(Create(tangent))
        self.play(tracker.animate.set_value(1.5), run_time=3, rate_func=there_and_back)
        self.wait(2)