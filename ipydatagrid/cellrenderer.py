#!/usr/bin/env python
# coding: utf-8

# Copyright (c) QuantStack.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from traitlets import (
    Any, Bool, Enum, Float, Instance, Unicode, Union, validate
)

from ipywidgets import Widget, widget_serialization, Color

# Dependency to bqplot is temporary, we should remove this dependency once scales are extracted from bqplot
from bqplot import Scale, ColorScale

from ._frontend import module_name, module_version
from .vegatranspiler.py2vega import python2vega_expr


class VegaExpr(Widget):
    _model_name = Unicode('VegaExprModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('VegaExprView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    value = Unicode('default_value').tag(sync=True)

    def __init__(self, value='', **kwargs):
        super(VegaExpr, self).__init__(value=value, **kwargs)


class Expr(VegaExpr):
    value = Any().tag(sync=True)

    @validate('value')
    def _validate_value(self, proposal):
        return python2vega_expr(proposal['value'], ['value', 'x', 'y', 'height', 'width', 'row', 'column'])


class CellRenderer(Widget):
    _model_name = Unicode('CellRendererModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('CellRendererView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)


class TextRenderer(CellRenderer):
    _model_name = Unicode('TextRendererModel').tag(sync=True)
    _view_name = Unicode('TextRendererView').tag(sync=True)

    font = Union((
        Unicode(), Instance(VegaExpr), Instance(Scale)
    ), default_value='12px sans-serif').tag(sync=True, **widget_serialization)
    text_color = Union((
        Color(), Instance(VegaExpr), Instance(ColorScale)
    ), default_value='black').tag(sync=True, **widget_serialization)
    background_color = Union((
        Color(), Instance(VegaExpr), Instance(ColorScale)
    ), default_value='white').tag(sync=True, **widget_serialization)
    vertical_alignment = Union((
        Enum(values=['top', 'center', 'bottom']), Instance(VegaExpr), Instance(Scale)
    ), default_value='center').tag(sync=True, **widget_serialization)
    horizontal_alignment = Union((
        Enum(values=['left', 'center', 'right']), Instance(VegaExpr), Instance(Scale)
    ), default_value='left').tag(sync=True, **widget_serialization)
    # format = Unicode(allow_none=True, default_value=None).tag(sync=True)


class BarRenderer(TextRenderer):
    _model_name = Unicode('BarRendererModel').tag(sync=True)
    _view_name = Unicode('BarRendererView').tag(sync=True)

    bar_color = Union((
        Color(), Instance(VegaExpr), Instance(ColorScale)
    ), default_value='#4682b4').tag(sync=True, **widget_serialization)
    value = Union((
        Float(), Instance(VegaExpr), Instance(Scale)
    ), default_value=0.).tag(sync=True, **widget_serialization)
    orientation = Union((
        Unicode(), Instance(VegaExpr), Instance(Scale)
    ), default_value='horizontal').tag(sync=True, **widget_serialization)
    bar_vertical_alignment = Union((
        Enum(values=['top', 'center', 'bottom']), Instance(VegaExpr), Instance(Scale)
    ), default_value='bottom').tag(sync=True, **widget_serialization)
    bar_horizontal_alignment = Union((
        Enum(values=['left', 'center', 'right']), Instance(VegaExpr), Instance(Scale)
    ), default_value='left').tag(sync=True, **widget_serialization)
    show_text = Union((
        Bool(), Instance(VegaExpr)
    ), default_value=True).tag(sync=True, **widget_serialization)
