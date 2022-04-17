import _plotly_utils.basevalidators


class ShowexponentValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="showexponent", parent_name="histogram2d.colorbar", **kwargs
    ):
        super(ShowexponentValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            values=kwargs.pop("values", ["all", "first", "last", "none"]),
            **kwargs,
        )
