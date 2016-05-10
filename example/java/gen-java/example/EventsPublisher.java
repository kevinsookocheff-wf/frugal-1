/**
 * Autogenerated by Frugal Compiler (1.3.1)
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *
 * @generated
 */

package example;

import com.workiva.frugal.middleware.InvocationHandler;
import com.workiva.frugal.middleware.ServiceMiddleware;
import com.workiva.frugal.protocol.*;
import com.workiva.frugal.provider.FScopeProvider;
import com.workiva.frugal.transport.FScopeTransport;
import com.workiva.frugal.transport.FSubscription;
import org.apache.thrift.TException;
import org.apache.thrift.TApplicationException;
import org.apache.thrift.transport.TTransportException;
import org.apache.thrift.protocol.*;

import javax.annotation.Generated;
import java.util.logging.Logger;




/**
 * This docstring gets added to the generated code because it has
 * the @ sign. Prefix specifies topic prefix tokens, which can be static or
 * variable.
 */
@Generated(value = "Autogenerated by Frugal Compiler (1.3.1)", date = "2016-5-10")
public class EventsPublisher {

	private static final String DELIMITER = ".";

	private final InternalEventsPublisher target;
	private final InternalEventsPublisher proxy;

	public EventsPublisher(FScopeProvider provider, ServiceMiddleware... middleware) {
		target = new InternalEventsPublisher(provider);
		proxy = (InternalEventsPublisher) InvocationHandler.composeMiddlewareClass(target, InternalEventsPublisher.class, middleware);
	}

	public void open() throws TException {
		target.open();
	}

	public void close() throws TException {
		target.close();
	}

	/**
	 * This is a docstring.
	 */
	public void publishEventCreated(FContext ctx, String user, Event req) throws TException {
		proxy.publishEventCreated(ctx, user, req);
	}

	protected static class InternalEventsPublisher {

		private FScopeProvider provider;
		private FScopeTransport transport;
		private FProtocol protocol;

		protected InternalEventsPublisher() {
		}

		public InternalEventsPublisher(FScopeProvider provider) {
			this.provider = provider;
		}

		public void open() throws TException {
			FScopeProvider.Client client = provider.build();
			transport = client.getTransport();
			protocol = client.getProtocol();
			transport.open();
		}

		public void close() throws TException {
			transport.close();
		}

		/**
		 * This is a docstring.
		 */
		public void publishEventCreated(FContext ctx, String user, Event req) throws TException {
			String op = "EventCreated";
			String prefix = String.format("foo.%s.", user);
			String topic = String.format("%sEvents%s%s", prefix, DELIMITER, op);
			transport.lockTopic(topic);
			try {
				protocol.writeRequestHeader(ctx);
				protocol.writeMessageBegin(new TMessage(op, TMessageType.CALL, 0));
				req.write(protocol);
				protocol.writeMessageEnd();
				transport.flush();
			} finally {
				transport.unlockTopic();
			}
		}
	}
}
