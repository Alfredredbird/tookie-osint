import configparser
import os
import subprocess

class PluginManager:

    def __init__(self, config_path='config/config.ini', plugins_dir='plugins'):
        self.config_path = config_path
        self.plugins_dir = plugins_dir
        self.config = self.load_config()

    # Read config.ini
    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)
        return config

    # Save the updated config to file
    def save_config(self):
        with open(self.config_path, 'w') as config_file:
            self.config.write(config_file)

    # Ensure 'Plugins' section exists, create it if not
    def update_plugins_in_config(self):
        if not self.config.has_section('Plugins'):
            self.config.add_section('Plugins')

        # List files in the /plugins/ directory
        plugin_files = [f for f in os.listdir(self.plugins_dir) if os.path.isfile(os.path.join(self.plugins_dir, f))]

        # Update the 'Plugins' section in the config
        for plugin_name in self.config.options('Plugins'):
            # Check if the corresponding file exists, remove entry if not found
            if f"{plugin_name}.py" not in plugin_files:
                self.config.remove_option('Plugins', plugin_name)

        # Add or update entries for existing files
        for plugin_file in plugin_files:
            # Remove file extension (assuming .py extension for plugins)
            plugin_name = os.path.splitext(plugin_file)[0]
            if not self.config.has_option('Plugins', plugin_name):
                # Check if the variable is already defined, if not, set 'true'
                self.config.set('Plugins', plugin_name, 'true')

        self.save_config()
        print("Config updated")

    # Update the status of the plugin only if it is not already defined
    def toggle_plugin_status(self, plugin_name, new_status):

        if self.config.has_section('Plugins') and self.config.has_option('Plugins', plugin_name):
            self.config.set('Plugins', plugin_name, str(new_status).lower())
            self.save_config()
            print(f"Status of {plugin_name} toggled to {new_status}")
        else:
            print(f"Plugin {plugin_name} not found in the config")

    # Check if all plugins are disabled
    def list_plugin_status(self):
        if self.config.has_section('Plugins'):
            all_disabled = all(not self.config.getboolean('Plugins', plugin_name, fallback=False)
                               for plugin_name in self.config.options('Plugins'))
            if all_disabled:
                print("All plugins are disabled.")
            else:
                for plugin_name in self.config.options('Plugins'):
                    plugin_status = self.config.getboolean('Plugins', plugin_name, fallback=False)
                    if plugin_status:
                        print(f"{plugin_name}: {'Enabled'}")
        else:
            print("No 'Plugins' section found in the config")

    # Print names and statuses of plugins that are enabled
    def print_and_run_plugins(self):
        if self.config.has_section('Plugins'):
            enabled_plugins = [plugin_name for plugin_name in self.config.options('Plugins')
                               if self.config.getboolean('Plugins', plugin_name, fallback=False)]

            if not enabled_plugins:
                print("All plugins are disabled.")
                return

            print("\nChoose a plugin to run:")
            for index, plugin_name in enumerate(enabled_plugins, start=1):
                print(f"[{index}] {plugin_name}")

            try:
                choice = int(input("Enter the number of the plugin to run: "))
                if 1 <= choice <= len(enabled_plugins):
                    selected_plugin = enabled_plugins[choice - 1]
                    plugin_dir = self.config.get('main', 'pluginfolder', fallback='plugins')
                    print(f"Running plugin: {selected_plugin}")
                    process = subprocess.Popen(['python', f'{plugin_dir}/{selected_plugin}.py'])
                    process.wait()
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("No 'Plugins' section found in the config")

# Initialization and example usage:
plugin_manager = PluginManager()
# plugin_manager.update_plugins_in_config()
# plugin_manager.list_plugin_status()
# plugin_manager.toggle_plugin_status('plugin1', True)
# plugin_manager.toggle_plugin_status('plugin2', False)
# plugin_manager.print_and_run_plugins()