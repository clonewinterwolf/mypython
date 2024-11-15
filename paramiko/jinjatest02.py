from jinja2 import Template, FileSystemLoader, Environment
import yaml

myyaml_file = "switch_data.yml"
template_dir = "./templates" 

template_env = Environment(loader=FileSystemLoader(template_dir), 
    trim_blocks = True,
    lstrip_blocks = True
    )

with open(myyaml_file, 'r') as yaml_file:
    try:
        yaml_data = yaml.safe_load(yaml_file)
    except yaml.YAMLError as exc:
        print(exc)

for device, config in yaml_data['dc1'].items():
    if config['device_template'] == "vIOSL2_Template":
        device_template = template_env.get_template("switch_day0_template.j2")
    elif config['device_template'] == "vIOSL3_Template":
        device_template = template_env.get_template("router_day0_template.j2")
    
    print(f".....rendering now device: {device}")
    day0_device_config = device_template.render(config)

    print(day0_device_config)