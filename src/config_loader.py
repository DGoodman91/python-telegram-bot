from jproperties import Properties


class ConfigLoader():
    """
    A class responsible for loading and validating application configuration
    """

    def load_app_config(self) -> dict[str, str]:
        """
        Returns a str->str dictionary containing application properties
        """
        
        configs = Properties()

        with open('config/app-config.properties', 'rb') as config_file:
            configs.load(config_file)

        self.validate(configs)

        return configs.properties

    def validate(self, configs: Properties) -> bool:
        """
        Validate the loaded application config.

        Returns True if all valid, else throws an exception
        """

        api_key = configs.get('api_key')
        if api_key == None:
            raise Exception(
                'API key not found - add to app-config.properties file w/ key \'api_key\'')

        return True
