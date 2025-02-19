from multipledispatch import dispatch
import random

class LoadBalancer:
    def __init__(self, platform):
        self.__platform = platform
        
    def __del__(self):
        pass

    @property
    def platform(self):
        return self.__platform

class ElasticLoadBalancer(LoadBalancer):
    def __init__(self, osi_level, name, target_group, listeners, internal):
        super().__init__("AWS")
        self.__osi_level = osi_level
        self.__internal = internal
        self.__logGroup = LogsGroup(name)
        self._target = target_group
        self._name = name
        self._listeners = {}
        self._attach(listeners)
    
    @property
    def osi_level(self):
        return self.__osi_level
    
    @property
    def internal(self):
        return self.__internal
    
    @property
    def logGroup(self):
        return self.__logGroup
    
    def __establish_listener(self, listener):
        print(f'Now LB listening requests on {listener} port')
    
    @dispatch(list)
    def _attach(self, multiple_listeners):
        for listener in multiple_listeners:
            self.__establish_listener(*listener)

    @dispatch(int)
    def _attach(self, listener):
        self.__establish_listener(listener)

class ApplicationLoadBalancer(ElasticLoadBalancer):
    def __init__(self, name, target, listeners, internal=False):
        super().__init__(7, name, target, listeners, internal)

class NetworkLoadBalancer(ElasticLoadBalancer):
    def __init__(self, name, target, listeners, internal=False):
        super().__init__(4, name, target, listeners, internal)

class GatewayLoadBalancer(ElasticLoadBalancer):
    def __init__(self, name, target, listeners, internal=False):
        super().__init__([3, 4, 7], name, target, listeners, internal)

class TargetGroup:
    __target_types = {"instance": 1, "ip": 2, "alb": 3, "lambda": 4}
    def __init__(self, type, value):
        self._target_type = self.get_type(type)
        self._connections = {}
        self._connect(value)

    def __del__(self):
        print("Target group was terminated")

    def get_type(self, type):
        type_id = self.__target_types.get(type)
        if type_id is None:
            raise ValueError("Invalid target type")
        return type_id
    
    def __establish_connection(self, target):
        established = random.randint(0, 1)
        if established:
            print(f'Established connection with {target}')
        else:
            print(f'Connection with {target} wasnt established')
        self._connections[target] = established

    @dispatch(list)
    def _connect(self, multiple_targets):
        for target in multiple_targets:
            self.__establish_connection(*target)

    @dispatch(str)
    def _connect(self, target):
        self.__establish_connection(target)

    @property
    def get_connections(self):
        return self._connections
    
class LogsGroup:
    def __init__(self, name):
        self._name = name
        self.__logs = "zero 500 http codes"

    def __del__(self):
        print("Log group was terminated")
    
    @property
    def logs(self):
        return self.__logs
    
prod_target = TargetGroup("ip", "10.0.0.12/24")
prod_alb = ApplicationLoadBalancer("prod-alb", prod_target, 80)

del prod_alb

prod_db_target = TargetGroup("instance", "main-rds-prod")
prod_nlb = NetworkLoadBalancer("prod", prod_db_target, 5432, True)

prod_api_gateway_target = TargetGroup("lambda", "gateway-script")
prod_glb = GatewayLoadBalancer("prod", prod_api_gateway_target, 5005, True)

del prod_target
