import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="y", parent_name="isosurface.colorbar", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 3),
            min=kwargs.pop("min", -2),
            **kwargs,
        )
