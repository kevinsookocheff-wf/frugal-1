#
# Autogenerated by Frugal Compiler (1.14.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import actual_base.python.ttypes

from ttypes import *
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol


class ping_args:
    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('ping_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class ping_result:
    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('ping_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class blah_args:
    """
    Attributes:
     - num
     - Str
     - event
    """
    def __init__(self, num=None, Str=None, event=None):
        self.num = num
        self.Str = Str
        self.event = event

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.num = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.Str = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.event = Event()
                    self.event.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('blah_args')
        if self.num is not None:
            oprot.writeFieldBegin('num', TType.I32, 1)
            oprot.writeI32(self.num)
            oprot.writeFieldEnd()
        if self.Str is not None:
            oprot.writeFieldBegin('Str', TType.STRING, 2)
            oprot.writeString(self.Str)
            oprot.writeFieldEnd()
        if self.event is not None:
            oprot.writeFieldBegin('event', TType.STRUCT, 3)
            self.event.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.num)
        value = (value * 31) ^ hash(self.Str)
        value = (value * 31) ^ hash(self.event)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class blah_result:
    """
    Attributes:
     - success
     - awe
     - api
    """
    def __init__(self, success=None, awe=None, api=None):
        self.success = success
        self.awe = awe
        self.api = api

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I64:
                    self.success = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.awe = AwesomeException()
                    self.awe.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.api = actual_base.python.ttypes.api_exception()
                    self.api.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('blah_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
            oprot.writeFieldEnd()
        if self.awe is not None:
            oprot.writeFieldBegin('awe', TType.STRUCT, 1)
            self.awe.write(oprot)
            oprot.writeFieldEnd()
        if self.api is not None:
            oprot.writeFieldBegin('api', TType.STRUCT, 2)
            self.api.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.success)
        value = (value * 31) ^ hash(self.awe)
        value = (value * 31) ^ hash(self.api)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class oneWay_args:
    """
    Attributes:
     - id
     - req
    """
    def __init__(self, id=None, req=None):
        self.id = id
        self.req = req

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.req = {}
                    (_, _, _elem42) = iprot.readMapBegin()
                    for _ in xrange(_elem42):
                        _elem44 = iprot.readI32()
                        _elem43 = iprot.readString()
                        self.req[_elem44] = _elem43
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('oneWay_args')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.I64, 1)
            oprot.writeI64(self.id)
            oprot.writeFieldEnd()
        if self.req is not None:
            oprot.writeFieldBegin('req', TType.MAP, 2)
            oprot.writeMapBegin(TType.I32, TType.STRING, len(self.req))
            for _elem46, _elem45 in self.req.items():
                oprot.writeI32(_elem46)
                oprot.writeString(_elem45)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.id)
        value = (value * 31) ^ hash(self.req)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class bin_method_args:
    """
    Attributes:
     - bin
     - Str
    """
    def __init__(self, bin=None, Str=None):
        self.bin = bin
        self.Str = Str

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.bin = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.Str = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('bin_method_args')
        if self.bin is not None:
            oprot.writeFieldBegin('bin', TType.STRING, 1)
            oprot.writeString(self.bin)
            oprot.writeFieldEnd()
        if self.Str is not None:
            oprot.writeFieldBegin('Str', TType.STRING, 2)
            oprot.writeString(self.Str)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.bin)
        value = (value * 31) ^ hash(self.Str)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class bin_method_result:
    """
    Attributes:
     - success
     - api
    """
    def __init__(self, success=None, api=None):
        self.success = success
        self.api = api

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.api = actual_base.python.ttypes.api_exception()
                    self.api.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('bin_method_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success)
            oprot.writeFieldEnd()
        if self.api is not None:
            oprot.writeFieldBegin('api', TType.STRUCT, 1)
            self.api.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.success)
        value = (value * 31) ^ hash(self.api)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class param_modifiers_args:
    """
    Attributes:
     - opt_num
     - default_num
     - req_num
    """
    def __init__(self, opt_num=None, default_num=None, req_num=None):
        self.opt_num = opt_num
        self.default_num = default_num
        self.req_num = req_num

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.opt_num = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.default_num = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.req_num = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('param_modifiers_args')
        if self.opt_num is not None:
            oprot.writeFieldBegin('opt_num', TType.I32, 1)
            oprot.writeI32(self.opt_num)
            oprot.writeFieldEnd()
        if self.default_num is not None:
            oprot.writeFieldBegin('default_num', TType.I32, 2)
            oprot.writeI32(self.default_num)
            oprot.writeFieldEnd()
        if self.req_num is not None:
            oprot.writeFieldBegin('req_num', TType.I32, 3)
            oprot.writeI32(self.req_num)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.req_num is None:
            raise TProtocol.TProtocolException(message='Required field req_num is unset!')
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.opt_num)
        value = (value * 31) ^ hash(self.default_num)
        value = (value * 31) ^ hash(self.req_num)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class param_modifiers_result:
    """
    Attributes:
     - success
    """
    def __init__(self, success=None):
        self.success = success

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I64:
                    self.success = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('param_modifiers_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.success)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class underlying_types_test_args:
    """
    Attributes:
     - list_type
     - set_type
    """
    def __init__(self, list_type=None, set_type=None):
        self.list_type = list_type
        self.set_type = set_type

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.list_type = []
                    (_, _elem47) = iprot.readListBegin()
                    for _ in xrange(_elem47):
                        _elem48 = iprot.readI64()
                        self.list_type.append(_elem48)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.SET:
                    self.set_type = set()
                    (_, _elem49) = iprot.readSetBegin()
                    for _ in xrange(_elem49):
                        _elem50 = iprot.readI64()
                        self.set_type.add(_elem50)
                    iprot.readSetEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('underlying_types_test_args')
        if self.list_type is not None:
            oprot.writeFieldBegin('list_type', TType.LIST, 1)
            oprot.writeListBegin(TType.I64, len(self.list_type))
            for _elem51 in self.list_type:
                oprot.writeI64(_elem51)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.set_type is not None:
            oprot.writeFieldBegin('set_type', TType.SET, 2)
            oprot.writeSetBegin(TType.I64, len(self.set_type))
            for _elem52 in self.set_type:
                oprot.writeI64(_elem52)
            oprot.writeSetEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.list_type)
        value = (value * 31) ^ hash(self.set_type)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class underlying_types_test_result:
    """
    Attributes:
     - success
    """
    def __init__(self, success=None):
        self.success = success

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_, _elem53) = iprot.readListBegin()
                    for _ in xrange(_elem53):
                        _elem54 = iprot.readI64()
                        self.success.append(_elem54)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('underlying_types_test_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.I64, len(self.success))
            for _elem55 in self.success:
                oprot.writeI64(_elem55)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.success)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.iteritems()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

