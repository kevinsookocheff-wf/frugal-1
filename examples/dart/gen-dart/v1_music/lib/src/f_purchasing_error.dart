// Autogenerated by Frugal Compiler (2.26.1)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

import 'dart:typed_data' show Uint8List;
import 'package:thrift/thrift.dart' as thrift;
import 'package:v1_music/v1_music.dart' as t_v1_music;

/// Exceptions are converted to the native format for each compiled
/// language.
class PurchasingError extends Error implements thrift.TBase {
  static final thrift.TStruct _STRUCT_DESC = new thrift.TStruct("PurchasingError");
  static final thrift.TField _MESSAGE_FIELD_DESC = new thrift.TField("message", thrift.TType.STRING, 1);
  static final thrift.TField _ERROR_CODE_FIELD_DESC = new thrift.TField("error_code", thrift.TType.I16, 2);

  String message;
  static const int MESSAGE = 1;
  int error_code = 0;
  static const int ERROR_CODE = 2;


  PurchasingError() {
  }

  @deprecated
  bool isSetMessage() => message != null;

  @deprecated
  unsetMessage() => message = null;

  @deprecated
  bool isSetError_code() => error_code != null;

  @deprecated
  unsetError_code() => error_code = null;

  @override
  getFieldValue(int fieldID) {
    switch (fieldID) {
      case MESSAGE:
        return this.message;
      case ERROR_CODE:
        return this.error_code;
      default:
        throw new ArgumentError("Field $fieldID doesn't exist!");
    }
  }

  @override
  setFieldValue(int fieldID, Object value) {
    switch (fieldID) {
      case MESSAGE:
        message = value as String; // ignore: avoid_as
        break;

      case ERROR_CODE:
        error_code = value as int; // ignore: avoid_as
        break;

      default:
        throw new ArgumentError("Field $fieldID doesn't exist!");
    }
  }

  // Returns true if the field corresponding to fieldID is set (has been assigned a value) and false otherwise
  @override
  bool isSet(int fieldID) {
    switch (fieldID) {
      case MESSAGE:
        return message != null;

      case ERROR_CODE:
        return error_code != null;

      default:
        throw new ArgumentError("Field $fieldID doesn't exist!");
    }
  }

  @override
  read(thrift.TProtocol iprot) {
    iprot.readStructBegin();
    for (thrift.TField field = iprot.readFieldBegin();
        field.type != thrift.TType.STOP;
        field = iprot.readFieldBegin()) {
      switch (field.id) {
        case MESSAGE:
          if (field.type == thrift.TType.STRING) {
            message = iprot.readString();
          } else {
            thrift.TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case ERROR_CODE:
          if (field.type == thrift.TType.I16) {
            error_code = iprot.readI16();
          } else {
            thrift.TProtocolUtil.skip(iprot, field.type);
          }
          break;
        default:
          thrift.TProtocolUtil.skip(iprot, field.type);
          break;
      }
      iprot.readFieldEnd();
    }
    iprot.readStructEnd();

    validate();
  }

  @override
  write(thrift.TProtocol oprot) {
    validate();

    oprot.writeStructBegin(_STRUCT_DESC);
    if (message != null) {
      oprot.writeFieldBegin(_MESSAGE_FIELD_DESC);
      oprot.writeString(message);
      oprot.writeFieldEnd();
    }
    oprot.writeFieldBegin(_ERROR_CODE_FIELD_DESC);
    oprot.writeI16(error_code);
    oprot.writeFieldEnd();
    oprot.writeFieldStop();
    oprot.writeStructEnd();
  }

  @override
  String toString() {
    StringBuffer ret = new StringBuffer("PurchasingError(");

    ret.write("message:");
    if (this.message == null) {
      ret.write("null");
    } else {
      ret.write(this.message);
    }

    ret.write(", ");
    ret.write("error_code:");
    ret.write(this.error_code);

    ret.write(")");

    return ret.toString();
  }

  @override
  bool operator ==(Object o) {
    if (o is PurchasingError) {
      return this.message == o.message &&
        this.error_code == o.error_code;
    }
    return false;
  }

  @override
  int get hashCode {
    var value = 17;
    value = (value * 31) ^ message.hashCode;
    value = (value * 31) ^ error_code.hashCode;
    return value;
  }

  PurchasingError clone({
    String message: null,
    int error_code: null,
  }) {
    return new PurchasingError()
      ..message = message ?? this.message
      ..error_code = error_code ?? this.error_code;
  }

  validate() {
  }
}
