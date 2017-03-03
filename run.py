# -*- encoding: utf-8 -*-

import os
import logging
import logging.config
import json
from webcron import setting

import click


def read_config(ctx, param, value):
    if not value:
        return {}

    def underline_dict(d):
        if not isinstance(d, dict):
            return d
        return dict((k.replace('-', '_'), underline_dict(v)) for k, v in d.items())

    config = underline_dict(json.load(value))
    ctx.default_map = config
    return config


@click.group()
@click.option('--logging-config', default=os.path.join(os.path.dirname(__file__), "logging.conf"),
              help="logging config file for built-in python logging module", show_default=True)
@click.option('--port', default=8000,
              help="web port", show_default=True)
@click.pass_context
def cli(ctx, **kwargs):
    logging_config = kwargs.pop('logging_config')
    logging.config.fileConfig(logging_config)
    ctx.obj = kwargs
    return ctx


@cli.command()
@click.pass_context
def web(ctx):
    g = ctx.obj
    g['module_name'] = 'web'
    g['logger'] = 'web'
    g['setting'] = setting.WEB_SETTINGS
    from webcron.urls import run
    run(g)


if __name__ == '__main__':
    cli()