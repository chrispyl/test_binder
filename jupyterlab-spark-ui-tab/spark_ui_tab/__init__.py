def _jupyter_server_extension_paths():
    """Used by "jupyter serverextension" command to install web server extension'"""
    return [{
        "module": "spark_ui_tab.serverextension"
    }]
