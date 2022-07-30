from src.middleware import request_cfg

class TenantRouter(object):
    def _default_db(self):
        if hasattr(request_cfg, 'cfg'):
            return request_cfg.cfg
        else:
            return 'default'

    def db_for_read(self, model, **hints):
        return self._default_db()

    def db_for_write(self, model, **hints):
        return self._default_db()

    def allow_relation(self, obj1, obj2, **hints):
        return True

