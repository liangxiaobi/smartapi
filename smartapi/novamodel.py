# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AgentBuilds(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    hypervisor = models.CharField(max_length=765, blank=True)
    os = models.CharField(max_length=765, blank=True)
    architecture = models.CharField(max_length=765, blank=True)
    version = models.CharField(max_length=765, blank=True)
    url = models.CharField(max_length=765, blank=True)
    md5hash = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'agent_builds'


class Aggregates(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, unique=True, blank=True)
    operational_state = models.CharField(max_length=765)
    availability_zone = models.CharField(max_length=765)
    class Meta:
        db_table = u'aggregates'
class AggregateHosts(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=765, unique=True, blank=True)
    aggregate = models.ForeignKey(Aggregates)
    class Meta:
        db_table = u'aggregate_hosts'
class AggregateMetadata(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    aggregate = models.ForeignKey(Aggregates)
    key = models.CharField(max_length=765)
    value = models.CharField(max_length=765)
    class Meta:
        db_table = u'aggregate_metadata'

class AuthTokens(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    token_hash = models.CharField(max_length=765, primary_key=True)
    user_id = models.CharField(max_length=765, blank=True)
    server_management_url = models.CharField(max_length=765, blank=True)
    storage_url = models.CharField(max_length=765, blank=True)
    cdn_management_url = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'auth_tokens'


class BwUsageCache(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    start_period = models.DateTimeField()
    last_refreshed = models.DateTimeField(null=True, blank=True)
    bw_in = models.BigIntegerField(null=True, blank=True)
    bw_out = models.BigIntegerField(null=True, blank=True)
    mac = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'bw_usage_cache'

class Cells(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    api_url = models.CharField(max_length=765, blank=True)
    username = models.CharField(max_length=765, blank=True)
    password = models.CharField(max_length=765, blank=True)
    weight_offset = models.FloatField(null=True, blank=True)
    weight_scale = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=765, blank=True)
    is_parent = models.IntegerField(null=True, blank=True)
    rpc_host = models.CharField(max_length=765, blank=True)
    rpc_port = models.IntegerField(null=True, blank=True)
    rpc_virtual_host = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'cells'

class Certificates(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=765, blank=True)
    project_id = models.CharField(max_length=765, blank=True)
    file_name = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'certificates'

class ComputeNodes(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    service_id = models.IntegerField()
    vcpus = models.IntegerField()
    memory_mb = models.IntegerField()
    local_gb = models.IntegerField()
    vcpus_used = models.IntegerField()
    memory_mb_used = models.IntegerField()
    local_gb_used = models.IntegerField()
    hypervisor_type = models.TextField()
    hypervisor_version = models.IntegerField()
    cpu_info = models.TextField()
    disk_available_least = models.IntegerField(null=True, blank=True)
    free_ram_mb = models.IntegerField(null=True, blank=True)
    free_disk_gb = models.IntegerField(null=True, blank=True)
    current_workload = models.IntegerField(null=True, blank=True)
    running_vms = models.IntegerField(null=True, blank=True)
    hypervisor_hostname = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'compute_nodes'

class ConsolePools(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=765, blank=True)
    username = models.CharField(max_length=765, blank=True)
    password = models.CharField(max_length=765, blank=True)
    console_type = models.CharField(max_length=765, blank=True)
    public_hostname = models.CharField(max_length=765, blank=True)
    host = models.CharField(max_length=765, blank=True)
    compute_host = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'console_pools'
class Instances(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    internal_id = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=765, blank=True)
    project_id = models.CharField(max_length=765, blank=True)
    image_ref = models.CharField(max_length=765, blank=True)
    kernel_id = models.CharField(max_length=765, blank=True)
    ramdisk_id = models.CharField(max_length=765, blank=True)
    server_name = models.CharField(max_length=765, blank=True)
    launch_index = models.IntegerField(null=True, blank=True)
    key_name = models.CharField(max_length=765, blank=True)
    key_data = models.TextField(blank=True)
    power_state = models.IntegerField(null=True, blank=True)
    vm_state = models.CharField(max_length=765, blank=True)
    memory_mb = models.IntegerField(null=True, blank=True)
    vcpus = models.IntegerField(null=True, blank=True)
    hostname = models.CharField(max_length=765, blank=True)
    host = models.CharField(max_length=765, blank=True)
    user_data = models.TextField(blank=True)
    reservation_id = models.CharField(max_length=765, blank=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    launched_at = models.DateTimeField(null=True, blank=True)
    terminated_at = models.DateTimeField(null=True, blank=True)
    display_name = models.CharField(max_length=765, blank=True)
    display_description = models.CharField(max_length=765, blank=True)
    availability_zone = models.CharField(max_length=765, blank=True)
    locked = models.IntegerField(null=True, blank=True)
    os_type = models.CharField(max_length=765, blank=True)
    launched_on = models.TextField(blank=True)
    instance_type_id = models.IntegerField(null=True, blank=True)
    vm_mode = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=108, unique=True, blank=True)
    architecture = models.CharField(max_length=765, blank=True)
    root_device_name = models.CharField(max_length=765, blank=True)
    access_ip_v4 = models.CharField(max_length=765, blank=True)
    access_ip_v6 = models.CharField(max_length=765, blank=True)
    config_drive = models.CharField(max_length=765, blank=True)
    task_state = models.CharField(max_length=765, blank=True)
    default_ephemeral_device = models.CharField(max_length=765, blank=True)
    default_swap_device = models.CharField(max_length=765, blank=True)
    progress = models.IntegerField(null=True, blank=True)
    auto_disk_config = models.IntegerField(null=True, blank=True)
    shutdown_terminate = models.IntegerField(null=True, blank=True)
    disable_terminate = models.IntegerField(null=True, blank=True)
    root_gb = models.IntegerField(null=True, blank=True)
    ephemeral_gb = models.IntegerField(null=True, blank=True)
    cell_name = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'instances'

class Consoles(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    instance_name = models.CharField(max_length=765, blank=True)
    instance_id = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=765, blank=True)
    port = models.IntegerField(null=True, blank=True)
    pool = models.ForeignKey(ConsolePools, null=True, blank=True)
    class Meta:
        db_table = u'consoles'


class FixedIps(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=765, blank=True)
    network_id = models.IntegerField(null=True, blank=True)
    instance_id = models.IntegerField(null=True, blank=True)
    allocated = models.IntegerField(null=True, blank=True)
    leased = models.IntegerField(null=True, blank=True)
    reserved = models.IntegerField(null=True, blank=True)
    virtual_interface_id = models.IntegerField(null=True, blank=True)
    host = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'fixed_ips'

class FloatingIps(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=765, blank=True)
    fixed_ip_id = models.IntegerField(null=True, blank=True)
    project_id = models.CharField(max_length=765, blank=True)
    host = models.CharField(max_length=765, blank=True)
    auto_assigned = models.IntegerField(null=True, blank=True)
    pool = models.CharField(max_length=765, blank=True)
    interface = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'floating_ips'

class InstanceActions(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    action = models.CharField(max_length=765, blank=True)
    error = models.TextField(blank=True)
    instance_uuid = models.CharField(max_length=108, blank=True)
    class Meta:
        db_table = u'instance_actions'

class InstanceFaults(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    instance_uuid = models.CharField(max_length=108, blank=True)
    code = models.IntegerField()
    message = models.CharField(max_length=765, blank=True)
    details = models.TextField(blank=True)
    class Meta:
        db_table = u'instance_faults'

class InstanceInfoCaches(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    network_info = models.TextField(blank=True)
    instance = models.ForeignKey(Instances,to_field='uuid', unique=True)
    class Meta:
        db_table = u'instance_info_caches'

class InstanceMetadata(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    instance = models.ForeignKey(Instances)
    key = models.CharField(max_length=765, blank=True)
    value = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'instance_metadata'


class InstanceTypes(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=765, blank=True)
    id = models.IntegerField(primary_key=True)
    memory_mb = models.IntegerField()
    vcpus = models.IntegerField()
    swap = models.IntegerField()
    vcpu_weight = models.IntegerField(null=True, blank=True)
    flavorid = models.CharField(max_length=765, blank=True)
    rxtx_factor = models.FloatField(null=True, blank=True)
    root_gb = models.IntegerField(null=True, blank=True)
    ephemeral_gb = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'instance_types'
class InstanceTypeExtraSpecs(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    instance_type = models.ForeignKey(InstanceTypes)
    key = models.CharField(max_length=765, blank=True)
    value = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'instance_type_extra_specs'




class KeyPairs(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    user_id = models.CharField(max_length=765, blank=True)
    fingerprint = models.CharField(max_length=765, blank=True)
    public_key = models.TextField(blank=True)
    class Meta:
        db_table = u'key_pairs'

class MigrateVersion(models.Model):
    repository_id = models.CharField(max_length=750, primary_key=True)
    repository_path = models.TextField(blank=True)
    version = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'migrate_version'

class Migrations(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    source_compute = models.CharField(max_length=765, blank=True)
    dest_compute = models.CharField(max_length=765, blank=True)
    dest_host = models.CharField(max_length=765, blank=True)
    status = models.CharField(max_length=765, blank=True)
    instance_uuid = models.CharField(max_length=765, blank=True)
    old_instance_type_id = models.IntegerField(null=True, blank=True)
    new_instance_type_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'migrations'

class Networks(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    injected = models.IntegerField(null=True, blank=True)
    cidr = models.CharField(max_length=765, blank=True)
    netmask = models.CharField(max_length=765, blank=True)
    bridge = models.CharField(max_length=765, blank=True)
    gateway = models.CharField(max_length=765, blank=True)
    broadcast = models.CharField(max_length=765, blank=True)
    dns1 = models.CharField(max_length=765, blank=True)
    vlan = models.IntegerField(null=True, blank=True)
    vpn_public_address = models.CharField(max_length=765, blank=True)
    vpn_public_port = models.IntegerField(null=True, blank=True)
    vpn_private_address = models.CharField(max_length=765, blank=True)
    dhcp_start = models.CharField(max_length=765, blank=True)
    project_id = models.CharField(max_length=765, blank=True)
    host = models.CharField(max_length=765, blank=True)
    cidr_v6 = models.CharField(max_length=765, blank=True)
    gateway_v6 = models.CharField(max_length=765, blank=True)
    label = models.CharField(max_length=765, blank=True)
    netmask_v6 = models.CharField(max_length=765, blank=True)
    bridge_interface = models.CharField(max_length=765, blank=True)
    multi_host = models.IntegerField(null=True, blank=True)
    dns2 = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=108, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    rxtx_base = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'networks'


class ProviderFwRules(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    protocol = models.CharField(max_length=15, blank=True)
    from_port = models.IntegerField(null=True, blank=True)
    to_port = models.IntegerField(null=True, blank=True)
    cidr = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'provider_fw_rules'

class Quotas(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    project_id = models.CharField(max_length=765, blank=True)
    resource = models.CharField(max_length=765)
    hard_limit = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'quotas'

class S3Images(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=108)
    class Meta:
        db_table = u's3_images'



class SecurityGroups(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    description = models.CharField(max_length=765, blank=True)
    user_id = models.CharField(max_length=765, blank=True)
    project_id = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'security_groups'
class SecurityGroupRules(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    parent_group = models.ForeignKey(SecurityGroups, null=True, blank=True)
    protocol = models.CharField(max_length=765, blank=True)
    from_port = models.IntegerField(null=True, blank=True)
    to_port = models.IntegerField(null=True, blank=True)
    cidr = models.CharField(max_length=765, blank=True)
    group = models.ForeignKey(SecurityGroups, null=True, blank=True)
    class Meta:
        db_table = u'security_group_rules'

        
class SecurityGroupInstanceAssociation(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    security_group = models.ForeignKey(SecurityGroups, null=True, blank=True)
    instance = models.ForeignKey(Instances, null=True, blank=True)
    class Meta:
        db_table = u'security_group_instance_association'

class Services(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=765, blank=True)
    binary = models.CharField(max_length=765, blank=True)
    topic = models.CharField(max_length=765, blank=True)
    report_count = models.IntegerField()
    disabled = models.IntegerField(null=True, blank=True)
    availability_zone = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'services'


class SmFlavors(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=765, blank=True)
    description = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'sm_flavors'
class SmBackendConfig(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    flavor = models.ForeignKey(SmFlavors)
    sr_uuid = models.CharField(max_length=765, blank=True)
    sr_type = models.CharField(max_length=765, blank=True)
    config_params = models.CharField(max_length=6141, blank=True)
    class Meta:
        db_table = u'sm_backend_config'


class Snapshots(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    volume_id = models.IntegerField()
    user_id = models.CharField(max_length=765, blank=True)
    project_id = models.CharField(max_length=765, blank=True)
    status = models.CharField(max_length=765, blank=True)
    progress = models.CharField(max_length=765, blank=True)
    volume_size = models.IntegerField(null=True, blank=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    display_name = models.CharField(max_length=765, blank=True)
    display_description = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'snapshots'



class Users(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.CharField(max_length=765, primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    access_key = models.CharField(max_length=765, blank=True)
    secret_key = models.CharField(max_length=765, blank=True)
    is_admin = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'users'

class VirtualInterfaces(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=765, unique=True, blank=True)
    network_id = models.IntegerField(null=True, blank=True)
    instance_id = models.IntegerField()
    uuid = models.CharField(max_length=108, blank=True)
    class Meta:
        db_table = u'virtual_interfaces'

class VirtualStorageArrays(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    display_name = models.CharField(max_length=765, blank=True)
    display_description = models.CharField(max_length=765, blank=True)
    project_id = models.CharField(max_length=765, blank=True)
    availability_zone = models.CharField(max_length=765, blank=True)
    instance_type_id = models.IntegerField()
    image_ref = models.CharField(max_length=765, blank=True)
    vc_count = models.IntegerField()
    vol_count = models.IntegerField()
    status = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'virtual_storage_arrays'



class VolumeTypes(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'volume_types'
class VolumeTypeExtraSpecs(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    volume_type = models.ForeignKey(VolumeTypes)
    key = models.CharField(max_length=765, blank=True)
    value = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'volume_type_extra_specs'

class Volumes(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    ec2_id = models.CharField(max_length=765, blank=True)
    user_id = models.CharField(max_length=765, blank=True)
    project_id = models.CharField(max_length=765, blank=True)
    host = models.CharField(max_length=765, blank=True)
    size = models.IntegerField(null=True, blank=True)
    availability_zone = models.CharField(max_length=765, blank=True)
    instance = models.ForeignKey(Instances, null=True, blank=True)
    mountpoint = models.CharField(max_length=765, blank=True)
    attach_time = models.CharField(max_length=765, blank=True)
    status = models.CharField(max_length=765, blank=True)
    attach_status = models.CharField(max_length=765, blank=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    launched_at = models.DateTimeField(null=True, blank=True)
    terminated_at = models.DateTimeField(null=True, blank=True)
    display_name = models.CharField(max_length=765, blank=True)
    display_description = models.CharField(max_length=765, blank=True)
    provider_location = models.CharField(max_length=768, blank=True)
    provider_auth = models.CharField(max_length=768, blank=True)
    snapshot_id = models.IntegerField(null=True, blank=True)
    volume_type_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'volumes'

class VolumeMetadata(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    volume = models.ForeignKey(Volumes)
    key = models.CharField(max_length=765, blank=True)
    value = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'volume_metadata'


class BlockDeviceMapping(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    instance = models.ForeignKey(Instances)
    device_name = models.CharField(max_length=765)
    delete_on_termination = models.IntegerField(null=True, blank=True)
    virtual_name = models.CharField(max_length=765, blank=True)
    snapshot = models.ForeignKey(Snapshots, null=True, blank=True)
    volume = models.ForeignKey(Volumes, null=True, blank=True)
    volume_size = models.IntegerField(null=True, blank=True)
    no_device = models.IntegerField(null=True, blank=True)
    connection_info = models.TextField(blank=True)
    class Meta:
        db_table = u'block_device_mapping'

class IscsiTargets(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    target_num = models.IntegerField(null=True, blank=True)
    host = models.CharField(max_length=765, blank=True)
    volume = models.ForeignKey(Volumes, null=True, blank=True)
    class Meta:
        db_table = u'iscsi_targets'
class Projects(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.CharField(max_length=765, primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    description = models.CharField(max_length=765, blank=True)
    project_manager = models.ForeignKey(Users, null=True, db_column='project_manager', blank=True)
    class Meta:
        db_table = u'projects'
class UserProjectAssociation(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(Users, primary_key=True)
    project = models.ForeignKey(Projects)
    class Meta:
        db_table = u'user_project_association'

class DnsDomains(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    domain = models.CharField(max_length=765, primary_key=True)
    scope = models.CharField(max_length=765, blank=True)
    availability_zone = models.CharField(max_length=765, blank=True)
    project = models.ForeignKey(Projects, null=True, blank=True)
    class Meta:
        db_table = u'dns_domains'
class SmVolume(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    id = models.ForeignKey(Volumes, primary_key=True, db_column='id')
    backend = models.ForeignKey(SmBackendConfig)
    vdi_uuid = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'sm_volume'
class UserProjectRoleAssociation(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(UserProjectAssociation, primary_key=True)
    project = models.ForeignKey(UserProjectAssociation, primary_key=True)
    role = models.CharField(max_length=765, primary_key=True)
    class Meta:
        db_table = u'user_project_role_association'

class UserRoleAssociation(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(Users, primary_key=True)
    role = models.CharField(max_length=765, primary_key=True)
    class Meta:
        db_table = u'user_role_association'
        
class InstanceMonitor(models.Model):
    '''
    virt-top time  16:57:40 Host sns x86_64 4/4CPU 1200MHz 7976MB 
   ID S RDRQ WRRQ RXBY TXBY %CPU %MEM   TIME    NAME
    '''
    uuid=models.CharField(max_length=765, primary_key=True)
    hosttime=models.DateTimeField(null=True,blank=True)
    host=models.CharField(max_length=100)
    rdrq=models.IntegerField()
    wrrq=models.IntegerField()
    txby=models.IntegerField()
    cpu=models.IntegerField()
    mem=models.IntegerField()
    vmtime=models.DateTimeField(null=True,blank=True)
