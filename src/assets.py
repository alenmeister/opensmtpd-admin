"""Bundle CSS and JS files"""

from flask import Flask
from flask_assets import Bundle, Environment


def compile_static_assets(app: Flask):
    """Configure static asset bundles"""

    assets_env = Environment(app)

    Environment.auto_build = True
    Environment.debug = False

    compile_stylesheets(assets_env)


def compile_stylesheets(assets_env: Environment):
    """Compile minified CSS bundles from SCSS styles"""

    main_scss_bundle = Bundle(
        'src/scss/main.scss',
        filters='pyscss',
        output='dist/css/main.min.css'
    )

    assets_env.register('main_scss_bundle', main_scss_bundle)
    main_scss_bundle.build()
