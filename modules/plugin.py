import configparser
import os
import subprocess

# Read config.ini
def pluginUpdater():
  config_path = 'config/config.ini'
  config = configparser.ConfigParser()
  config.read(config_path)

  # Ensure 'Plugins' section exists, create it if not
  if not config.has_section('Plugins'):
      config.add_section('Plugins')

  # List files in the /plugins/ directory
  plugins_dir = 'plugins'
  plugin_files = [f for f in os.listdir(plugins_dir) if os.path.isfile(os.path.join(plugins_dir, f))]

  # Update the 'Plugins' section in the config
  for plugin_name in config.options('Plugins'):
      # Check if the corresponding file exists, remove entry if not found
      if f"{plugin_name}.py" not in plugin_files:
          config.remove_option('Plugins', plugin_name)

  # Add or update entries for existing files
  for plugin_file in plugin_files:
      # Remove file extension (assuming .py extension for plugins)
      plugin_name = os.path.splitext(plugin_file)[0]

      # Check if the variable is already defined, if not, set 'true'
      if not config.has_option('Plugins', plugin_name):
          config.set('Plugins', plugin_name, 'true')

  # Save the updated config to file
  with open(config_path, 'w') as config_file:
      config.write(config_file)

  print("Config updated")


def toggle_plugin_status(plugin_name, new_status):
    # Read config.ini
    config_path = 'config/config.ini'
    config = configparser.ConfigParser()
    config.read(config_path)

    # Ensure 'Plugins' section exists, create it if not
    if not config.has_section('Plugins'):
        config.add_section('Plugins')

    # Check if the plugin exists in the config
    if config.has_option('Plugins', plugin_name):
        # Update the status of the plugin only if it is not already defined
        if not config.getboolean('Plugins', plugin_name, fallback=False):
            config.set('Plugins', plugin_name, str(new_status).lower())
            print(f"Status of {plugin_name} toggled to {new_status}")

            # Save the updated config to file
            with open(config_path, 'w') as config_file:
                config.write(config_file)
        else:
            print(f"Plugin {plugin_name} is already defined in the config")
    else:
        print(f"Plugin {plugin_name} not found in the config")


def list_plugin_status():
    # Read config.ini
    config_path = 'config/config.ini'
    config = configparser.ConfigParser()
    config.read(config_path)

    # Ensure 'Plugins' section exists
    if config.has_section('Plugins'):
        # Check if all plugins are disabled
        all_disabled = all(not config.getboolean('Plugins', plugin_name, fallback=False) for plugin_name in config.options('Plugins'))

        if all_disabled:
            print("All plugins are disabled.")
        else:
            # Print names and statuses of plugins that are enabled
            for plugin_name in config.options('Plugins'):
                plugin_status = config.getboolean('Plugins', plugin_name, fallback=False)
                if plugin_status:
                    print(f"{plugin_name}: {'Enabled'}")
    else:
        print("No 'Plugins' section found in the config")


def print_and_run_plugins():
    # Read config.ini
    config_path = 'config/config.ini'
    config = configparser.ConfigParser()
    config.read(config_path)

    # Ensure 'Plugins' section exists
    if config.has_section('Plugins'):
        enabled_plugins = [plugin_name for plugin_name in config.options('Plugins')
                           if config.getboolean('Plugins', plugin_name, fallback=False)]

        if not enabled_plugins:
            print("All plugins are disabled.")
            return
        print()
        print("Choose a plugin to run:")
        for index, plugin_name in enumerate(enabled_plugins, start=1):
            print(f"[{index}] {plugin_name}")

        try:
            choice = int(input("Enter the number of the plugin to run: "))
            if 1 <= choice <= len(enabled_plugins):
                selected_plugin = enabled_plugins[choice - 1]
                plugin_dir = config.get('main', 'pluginfolder')
                print(f"Running plugin: {selected_plugin}")
                if os.name == 'nt':
                 process = subprocess.Popen(['python.exe', f'{plugin_dir}/{selected_plugin}.py'])
                else:
                 process = subprocess.Popen(['python3', f'{plugin_dir}/{selected_plugin}.py']) 
                process.wait()

            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No 'Plugins' section found in the config")