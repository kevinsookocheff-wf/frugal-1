// Autogenerated by Frugal Compiler (1.3.1)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

library valid.src.f_blah_scope;

import 'dart:async';

import 'package:thrift/thrift.dart' as thrift;
import 'package:frugal/frugal.dart' as frugal;

import 'package:valid/valid.dart' as t_valid;


const String delimiter = '.';

class BlahPublisher {
  frugal.FScopeTransport fTransport;
  frugal.FProtocol fProtocol;
  BlahPublisher(frugal.FScopeProvider provider) {
    fTransport = provider.fTransportFactory.getTransport();
    fProtocol = provider.fProtocolFactory.getProtocol(fTransport);
  }

  Future open() {
    return fTransport.open();
  }

  Future close() {
    return fTransport.close();
  }

  Future publishDoStuff(frugal.FContext ctx, t_valid.Thing req) async {
    var op = "DoStuff";
    var prefix = "";
    var topic = "${prefix}Blah${delimiter}${op}";
    fTransport.setTopic(topic);
    var oprot = fProtocol;
    var msg = new thrift.TMessage(op, thrift.TMessageType.CALL, 0);
    oprot.writeRequestHeader(ctx);
    oprot.writeMessageBegin(msg);
    req.write(oprot);
    oprot.writeMessageEnd();
    await oprot.transport.flush();
  }
}


class BlahSubscriber {
  final frugal.FScopeProvider provider;

  BlahSubscriber(this.provider) {}

  Future<frugal.FSubscription> subscribeDoStuff(dynamic onThing(frugal.FContext ctx, t_valid.Thing req)) async {
    var op = "DoStuff";
    var prefix = "";
    var topic = "${prefix}Blah${delimiter}${op}";
    var transport = provider.fTransportFactory.getTransport();
    await transport.subscribe(topic, _recvDoStuff(op, provider.fProtocolFactory, onThing));
    return new frugal.FSubscription(topic, transport);
  }

  _recvDoStuff(String op, frugal.FProtocolFactory protocolFactory, dynamic onThing(frugal.FContext ctx, t_valid.Thing req)) {
    callbackDoStuff(thrift.TTransport transport) {
      var iprot = protocolFactory.getProtocol(transport);
      var ctx = iprot.readRequestHeader();
      var tMsg = iprot.readMessageBegin();
      if (tMsg.name != op) {
        thrift.TProtocolUtil.skip(iprot, thrift.TType.STRUCT);
        iprot.readMessageEnd();
        throw new thrift.TApplicationError(
        thrift.TApplicationErrorType.UNKNOWN_METHOD, tMsg.name);
      }
      var req = new t_valid.Thing();
      req.read(iprot);
      iprot.readMessageEnd();
      onThing(ctx, req);
    }
    return callbackDoStuff;
  }
}

