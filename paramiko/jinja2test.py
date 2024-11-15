from jinja2 import Template, FileSystemLoader, Environment
import yaml

with open("switch_data.yml", 'r') as yaml_file:
    try:
        yaml_data = yaml.safe_load(yaml_file)
    except yaml.YAMLError as exc:
        print(exc)


router_template = Template("hostname {{ hostname }}\n aaa new-model\n int {{mgmt_intf}}\n ip address {{mgmt_ip}}\n {{mgmt_subnet}}\n")
switch_template = Template("hostname {{ hostname }}\n aaa new-model\n int {{mgmt_intf}}\n ip address {{mgmt_ip}}\n {{mgmt_subnet}}\n")

for device, config in yaml_data['dc1'].items():
    if config['device_template'] == "vIOSL2_Template":
        device_template = router_template
    elif config['device_template'] == "vIOSL3_Template":
        device_template = switch_template
    
    print("rendering now device{0}".format(device))
    day0_device_config = device_template.render(config)

    print(day0_device_config)

#sw1={'hostname':"switch01", 'mgmt_intf':'gig0/0', 'mgmt_ip':'10.10.8.111','mgmt_subnet':'255.255.255.0'}
#print(template.render(sw1))
