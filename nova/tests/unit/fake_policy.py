# Copyright (c) 2012 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


policy_data = """
{
    "admin_api": "is_admin:True",

    "cells_scheduler_filter:TargetCellFilter": "is_admin:True",

    "context_is_admin": "role:admin or role:administrator",
    "compute:create": "",
    "compute:create:attach_network": "",
    "compute:create:attach_volume": "",

    "compute:get": "",
    "compute:get_all": "",
    "compute:get_all_tenants": "",

    "compute:update": "",

    "compute:get_instance_metadata": "",
    "compute:get_all_instance_metadata": "",
    "compute:get_all_instance_system_metadata": "",
    "compute:update_instance_metadata": "",
    "compute:delete_instance_metadata": "",

    "compute:get_instance_faults": "",
    "compute:get_diagnostics": "",
    "compute:get_instance_diagnostics": "",

    "compute:get_lock": "",
    "compute:lock": "",
    "compute:unlock": "",
    "compute:unlock_override": "is_admin:True",

    "compute:get_vnc_console": "",
    "compute:get_spice_console": "",
    "compute:get_rdp_console": "",
    "compute:get_serial_console": "",
    "compute:get_console_output": "",

    "compute:associate_floating_ip": "",
    "compute:reset_network": "",
    "compute:inject_network_info": "",
    "compute:add_fixed_ip": "",
    "compute:remove_fixed_ip": "",

    "compute:attach_volume": "",
    "compute:detach_volume": "",

    "compute:attach_interface": "",
    "compute:detach_interface": "",

    "compute:set_admin_password": "",

    "compute:rescue": "",
    "compute:unrescue": "",

    "compute:suspend": "",
    "compute:resume": "",

    "compute:pause": "",
    "compute:unpause": "",

    "compute:start": "",
    "compute:stop": "",

    "compute:resize": "",
    "compute:confirm_resize": "",
    "compute:revert_resize": "",

    "compute:rebuild": "",

    "compute:reboot": "",

    "compute:snapshot": "",
    "compute:snapshot_volume_backed": "",
    "compute:backup": "",

    "compute:shelve": "",
    "compute:shelve_offload": "",
    "compute:unshelve": "",

    "compute:security_groups:add_to_instance": "",
    "compute:security_groups:remove_from_instance": "",

    "compute:delete": "",
    "compute:soft_delete": "",
    "compute:force_delete": "",
    "compute:restore": "",
    "compute:swap_volume": "",

    "compute:volume_snapshot_create": "",
    "compute:volume_snapshot_delete": "",

    "os_compute_api:servers:confirm_resize": "",
    "os_compute_api:servers:create": "",
    "os_compute_api:servers:create:attach_network": "",
    "os_compute_api:servers:create:attach_volume": "",
    "os_compute_api:servers:create:forced_host": "",
    "os_compute_api:servers:delete": "",
    "os_compute_api:servers:detail": "",
    "os_compute_api:servers:detail:get_all_tenants": "",
    "os_compute_api:servers:index": "",
    "os_compute_api:servers:index:get_all_tenants": "",
    "os_compute_api:servers:reboot": "",
    "os_compute_api:servers:rebuild": "",
    "os_compute_api:servers:resize": "",
    "os_compute_api:servers:revert_resize": "",
    "os_compute_api:servers:show": "",
    "os_compute_api:servers:create_image": "",
    "os_compute_api:servers:create_image:allow_volume_backed": "",
    "os_compute_api:servers:update": "",
    "os_compute_api:servers:start": "",
    "os_compute_api:servers:stop": "",
    "os_compute_api:os-access-ips": "",
    "compute_extension:accounts": "",
    "compute_extension:admin_actions:pause": "",
    "compute_extension:admin_actions:unpause": "",
    "compute_extension:admin_actions:suspend": "",
    "compute_extension:admin_actions:resume": "",
    "compute_extension:admin_actions:lock": "",
    "compute_extension:admin_actions:unlock": "",
    "compute_extension:admin_actions:resetNetwork": "",
    "compute_extension:admin_actions:injectNetworkInfo": "",
    "compute_extension:admin_actions:createBackup": "",
    "compute_extension:admin_actions:migrateLive": "",
    "compute_extension:admin_actions:resetState": "",
    "compute_extension:admin_actions:migrate": "",
    "os_compute_api:os-admin-actions:reset_network": "",
    "os_compute_api:os-admin-actions:inject_network_info": "",
    "os_compute_api:os-admin-actions:reset_state": "",
    "os_compute_api:os-admin-password": "",
    "compute_extension:aggregates": "rule:admin_api",
    "os_compute_api:os-aggregates:index": "rule:admin_api",
    "os_compute_api:os-aggregates:create": "rule:admin_api",
    "os_compute_api:os-aggregates:show": "rule:admin_api",
    "os_compute_api:os-aggregates:update": "rule:admin_api",
    "os_compute_api:os-aggregates:delete": "rule:admin_api",
    "os_compute_api:os-aggregates:add_host": "rule:admin_api",
    "os_compute_api:os-aggregates:remove_host": "rule:admin_api",
    "os_compute_api:os-aggregates:set_metadata": "rule:admin_api",
    "compute_extension:agents": "",
    "os_compute_api:os-agents": "",
    "compute_extension:attach_interfaces": "",
    "os_compute_api:os-attach-interfaces": "",
    "compute_extension:baremetal_nodes": "",
    "os_compute_api:os-baremetal-nodes": "",
    "compute_extension:cells": "",
    "compute_extension:cells:create": "rule:admin_api",
    "compute_extension:cells:delete": "rule:admin_api",
    "compute_extension:cells:update": "rule:admin_api",
    "compute_extension:cells:sync_instances": "rule:admin_api",
    "os_compute_api:os-cells": "",
    "os_compute_api:os-cells:create": "rule:admin_api",
    "os_compute_api:os-cells:delete": "rule:admin_api",
    "os_compute_api:os-cells:update": "rule:admin_api",
    "os_compute_api:os-cells:sync_instances": "rule:admin_api",
    "compute_extension:certificates": "",
    "os_compute_api:os-certificates:create": "",
    "os_compute_api:os-certificates:show": "",
    "compute_extension:cloudpipe": "",
    "os_compute_api:os-cloudpipe": "",
    "compute_extension:cloudpipe_update": "",
    "compute_extension:config_drive": "",
    "os_compute_api:os-config-drive": "",
    "compute_extension:console_output": "",
    "os_compute_api:os-console-output": "",
    "compute_extension:consoles": "",
    "os_compute_api:os-remote-consoles": "",
    "os_compute_api:os-consoles": "",
    "os_compute_api:os-consoles:create": "",
    "os_compute_api:os-consoles:delete": "",
    "os_compute_api:os-consoles:index": "",
    "os_compute_api:os-consoles:show": "",
    "compute_extension:createserverext": "",
    "os_compute_api:os-create-backup": "",
    "compute_extension:deferred_delete": "",
    "os_compute_api:os-deferred-delete": "",
    "compute_extension:disk_config": "",
    "os_compute_api:os-disk-config": "",
    "compute_extension:evacuate": "is_admin:True",
    "os_compute_api:os-evacuate": "is_admin:True",
    "compute_extension:extended_server_attributes": "",
    "os_compute_api:os-extended-server-attributes": "",
    "compute_extension:extended_status": "",
    "os_compute_api:os-extended-status": "",
    "compute_extension:extended_availability_zone": "",
    "os_compute_api:os-extended-availability-zone": "",
    "compute_extension:extended_ips": "",
    "compute_extension:extended_ips_mac": "",
    "compute_extension:extended_vif_net": "",
    "compute_extension:extended_volumes": "",
    "os_compute_api:ips:index": "",
    "os_compute_api:ips:show": "",
    "os_compute_api:os-extended-volumes": "",
    "os_compute_api:extensions": "",
    "os_compute_api:extensions:discoverable": "",
    "compute_extension:fixed_ips": "",
    "os_compute_api:os-fixed-ips": "",
    "compute_extension:flavor_access": "",
    "compute_extension:flavor_access:addTenantAccess": "",
    "compute_extension:flavor_access:removeTenantAccess": "",
    "os_compute_api:os-flavor-access": "",
    "os_compute_api:os-flavor-access:remove_tenant_access": "",
    "os_compute_api:os-flavor-access:add_tenant_access": "",
    "compute_extension:flavor_disabled": "",
    "os_compute_api:os-flavor-disabled": "",
    "compute_extension:flavor_rxtx": "",
    "os_compute_api:os-flavor-rxtx": "",
    "compute_extension:flavor_swap": "",
    "compute_extension:flavorextradata": "",
    "compute_extension:flavorextraspecs:index": "",
    "compute_extension:flavorextraspecs:show": "",
    "compute_extension:flavorextraspecs:create": "is_admin:True",
    "compute_extension:flavorextraspecs:update": "is_admin:True",
    "compute_extension:flavorextraspecs:delete": "is_admin:True",
    "os_compute_api:os-flavor-extra-specs:index": "",
    "os_compute_api:os-flavor-extra-specs:show": "",
    "os_compute_api:os-flavor-extra-specs:create": "is_admin:True",
    "os_compute_api:os-flavor-extra-specs:update": "is_admin:True",
    "os_compute_api:os-flavor-extra-specs:delete": "is_admin:True",
    "compute_extension:flavormanage": "",
    "os_compute_api:os-flavor-manage": "",
    "os_compute_api:os-flavors:discoverable": "",
    "compute_extension:floating_ip_dns": "",
    "os_compute_api:os-floating-ip-dns": "",
    "os_compute_api:os-floating-ip-dns:domain:update": "",
    "os_compute_api:os-floating-ip-dns:domain:delete": "",
    "compute_extension:floating_ip_pools": "",
    "os_compute_api:os-floating-ip-pools": "",
    "compute_extension:floating_ips": "",
    "os_compute_api:os-floating-ips": "",
    "compute_extension:floating_ips_bulk": "",
    "os_compute_api:os-floating-ips-bulk": "",
    "compute_extension:fping": "",
    "compute_extension:fping:all_tenants": "is_admin:True",
    "os_compute_api:os-fping": "",
    "os_compute_api:os-fping:all_tenants": "is_admin:True",
    "compute_extension:hide_server_addresses": "",
    "os_compute_api:os-hide-server-addresses": "",
    "compute_extension:hosts": "",
    "os_compute_api:os-hosts": "rule:admin_api",
    "compute_extension:hypervisors": "rule:admin_api",
    "os_compute_api:os-hypervisors": "rule:admin_api",
    "compute_extension:image_size": "",
    "os_compute_api:image-size": "",
    "compute_extension:instance_actions": "",
    "os_compute_api:os-instance-actions": "",
    "compute_extension:instance_actions:events": "is_admin:True",
    "os_compute_api:os-instance-actions:events": "is_admin:True",
    "compute_extension:instance_usage_audit_log": "rule:admin_api",
    "os_compute_api:os-instance-usage-audit-log": "",
    "compute_extension:keypairs": "",
    "compute_extension:keypairs:index": "",
    "compute_extension:keypairs:show": "",
    "compute_extension:keypairs:create": "",
    "compute_extension:keypairs:delete": "",

    "os_compute_api:os-keypairs": "",
    "os_compute_api:os-keypairs:index": "",
    "os_compute_api:os-keypairs:show": "",
    "os_compute_api:os-keypairs:create": "",
    "os_compute_api:os-keypairs:delete": "",
    "os_compute_api:os-lock-server:lock": "",
    "os_compute_api:os-lock-server:unlock": "",
    "os_compute_api:os-lock-server:unlock:unlock_override": "",
    "os_compute_api:os-migrate-server:migrate": "",
    "os_compute_api:os-migrate-server:migrate_live": "",
    "compute_extension:multinic": "",
    "os_compute_api:os-multinic": "",
    "compute_extension:networks": "",
    "compute_extension:networks:view": "",
    "os_compute_api:os-networks": "",
    "os_compute_api:os-networks:view": "",
    "compute_extension:networks_associate": "",
    "os_compute_api:os-networks-associate": "",
    "compute_extension:os-tenant-networks": "",
    "os_compute_api:os-tenant-networks": "",
    "os_compute_api:os-pause-server:pause": "",
    "os_compute_api:os-pause-server:unpause": "",
    "os_compute_api:os-pci:pci_servers": "",
    "os_compute_api:os-pci:index": "",
    "os_compute_api:os-pci:detail": "",
    "os_compute_api:os-pci:show": "",
    "compute_extension:quotas:show": "",
    "compute_extension:quotas:update": "",
    "compute_extension:quotas:delete": "",
    "os_compute_api:os-quota-sets:show": "",
    "os_compute_api:os-quota-sets:update": "",
    "os_compute_api:os-quota-sets:delete": "",
    "os_compute_api:os-quota-sets:detail": "",
    "os_compute_api:os-quota-sets:defaults": "",
    "compute_extension:quota_classes": "",
    "os_compute_api:os-quota-class-sets": "",
    "compute_extension:rescue": "",
    "os_compute_api:os-rescue": "",
    "compute_extension:security_group_default_rules": "",
    "os_compute_api:os-security-group-default-rules": "",
    "compute_extension:security_groups": "",
    "os_compute_api:os-security-groups": "",
    "compute_extension:server_diagnostics": "",
    "os_compute_api:os-server-diagnostics": "",
    "compute_extension:server_groups": "",
    "compute_extension:server_password": "",
    "os_compute_api:os-server-password": "",
    "compute_extension:server_usage": "",
    "os_compute_api:os-server-usage": "",
    "os_compute_api:os-server-groups": "",
    "compute_extension:services": "",
    "os_compute_api:os-services": "",
    "compute_extension:shelve": "",
    "compute_extension:shelveOffload": "",
    "os_compute_api:os-shelve:shelve": "",
    "os_compute_api:os-shelve:shelve_offload": "",
    "compute_extension:simple_tenant_usage:show": "",
    "compute_extension:simple_tenant_usage:list": "",
    "os_compute_api:os-simple-tenant-usage:show": "",
    "os_compute_api:os-simple-tenant-usage:list": "",
    "compute_extension:unshelve": "",
    "os_compute_api:os-shelve:unshelve": "",
    "os_compute_api:os-suspend-server:suspend": "",
    "os_compute_api:os-suspend-server:resume": "",
    "compute_extension:users": "",
    "compute_extension:virtual_interfaces": "",
    "os_compute_api:os-virtual-interfaces": "",
    "compute_extension:virtual_storage_arrays": "",
    "compute_extension:volumes": "",
    "compute_extension:volume_attachments:index": "",
    "compute_extension:volume_attachments:show": "",
    "compute_extension:volume_attachments:create": "",
    "compute_extension:volume_attachments:update": "",
    "compute_extension:volume_attachments:delete": "",
    "os_compute_api:os-volumes": "",
    "os_compute_api:os-volumes-attachments:index": "",
    "os_compute_api:os-volumes-attachments:show": "",
    "os_compute_api:os-volumes-attachments:create": "",
    "os_compute_api:os-volumes-attachments:update": "",
    "os_compute_api:os-volumes-attachments:delete": "",
    "compute_extension:volumetypes": "",
    "compute_extension:zones": "",
    "compute_extension:availability_zone:list": "",
    "os_compute_api:os-availability-zone:list": "",
    "compute_extension:availability_zone:detail": "",
    "os_compute_api:os-availability-zone:detail": "",
    "compute_extension:used_limits_for_admin": "is_admin:True",
    "os_compute_api:os-used-limits": "is_admin:True",
    "compute_extension:migrations:index": "is_admin:True",
    "os_compute_api:os-migrations:index": "is_admin:True",
    "compute_extension:os-assisted-volume-snapshots:create": "",
    "compute_extension:os-assisted-volume-snapshots:delete": "",
    "os_compute_api:os-assisted-volume-snapshots:create": "",
    "os_compute_api:os-assisted-volume-snapshots:delete": "",
    "compute_extension:console_auth_tokens": "is_admin:True",
    "os_compute_api:os-console-auth-tokens": "is_admin:True",
    "compute_extension:os-server-external-events:create": "rule:admin_api",
    "os_compute_api:os-server-external-events:create": "rule:admin_api",
    "os_compute_api:server-metadata:create": "",
    "os_compute_api:server-metadata:update": "",
    "os_compute_api:server-metadata:update_all": "",
    "os_compute_api:server-metadata:delete": "",
    "os_compute_api:server-metadata:show": "",
    "os_compute_api:server-metadata:index": "",

    "network:get_all": "",
    "network:get": "",
    "network:create": "",
    "network:delete": "",
    "network:associate": "",
    "network:disassociate": "",
    "network:get_vifs_by_instance": "",
    "network:get_vif_by_mac_address": "",
    "network:allocate_for_instance": "",
    "network:deallocate_for_instance": "",
    "network:validate_networks": "",
    "network:get_instance_uuids_by_ip_filter": "",
    "network:get_instance_id_by_floating_address": "",
    "network:setup_networks_on_host": "",

    "network:get_floating_ip": "",
    "network:get_floating_ip_pools": "",
    "network:get_floating_ip_by_address": "",
    "network:get_floating_ips_by_project": "",
    "network:get_floating_ips_by_fixed_address": "",
    "network:allocate_floating_ip": "",
    "network:associate_floating_ip": "",
    "network:disassociate_floating_ip": "",
    "network:release_floating_ip": "",
    "network:migrate_instance_start": "",
    "network:migrate_instance_finish": "",

    "network:get_fixed_ip": "",
    "network:get_fixed_ip_by_address": "",
    "network:add_fixed_ip_to_instance": "",
    "network:remove_fixed_ip_from_instance": "",
    "network:add_network_to_project": "",
    "network:get_instance_nw_info": "",

    "network:get_dns_domains": "",
    "network:add_dns_entry": "",
    "network:modify_dns_entry": "",
    "network:delete_dns_entry": "",
    "network:get_dns_entries_by_address": "",
    "network:get_dns_entries_by_name": "",
    "network:create_private_dns_domain": "",
    "network:create_public_dns_domain": "",
    "network:delete_dns_domain": "",
    "network:attach_external_network": "rule:admin_api"
}
"""
