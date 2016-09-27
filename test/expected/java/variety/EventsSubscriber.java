/**
 * Autogenerated by Frugal Compiler (1.19.0)
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *
 * @generated
 */

package variety.java;

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




@Generated(value = "Autogenerated by Frugal Compiler (1.19.0)", date = "2015-11-24")
public class EventsSubscriber {

	/**
	 * This docstring gets added to the generated code because it has
	 * the @ sign. Prefix specifies topic prefix tokens, which can be static or
	 * variable.
	 */
	public interface Iface {
		/**
		 * This is a docstring.
		 */
		public FSubscription subscribeEventCreated(String user, final EventCreatedHandler handler) throws TException;

	}

	public interface EventCreatedHandler {
		void onEventCreated(FContext ctx, Event req);
	}

	/**
	 * This docstring gets added to the generated code because it has
	 * the @ sign. Prefix specifies topic prefix tokens, which can be static or
	 * variable.
	 */
	public static class Client implements Iface {
		private static final String DELIMITER = ".";
		private static final Logger LOGGER = Logger.getLogger(Client.class.getName());

		private final FScopeProvider provider;
		private final ServiceMiddleware[] middleware;

		public Client(FScopeProvider provider, ServiceMiddleware... middleware) {
			this.provider = provider;
			this.middleware = middleware;
		}

		/**
		 * This is a docstring.
		 */
		public FSubscription subscribeEventCreated(String user, final EventCreatedHandler handler) throws TException {
			final String op = "EventCreated";
			String prefix = String.format("foo.%s.", user);
			final String topic = String.format("%sEvents%s%s", prefix, DELIMITER, op);
			final FScopeProvider.Client client = provider.build();
			final FScopeTransport transport = client.getTransport();
			transport.subscribe(topic);

			final EventCreatedHandler proxiedHandler = InvocationHandler.composeMiddleware(handler, EventCreatedHandler.class, middleware);
			final FSubscription sub = FSubscription.of(topic, transport);
			new Thread(new Runnable() {
				public void run() {
					while (true) {
						try {
							FContext ctx = client.getProtocol().readRequestHeader();
							Event received = recvEventCreated(op, client.getProtocol());
							proxiedHandler.onEventCreated(ctx, received);
						} catch (TException e) {
							if (e instanceof TTransportException) {
								TTransportException transportException = (TTransportException) e;
								if (transportException.getType() == TTransportException.END_OF_FILE) {
									return;
								}
							}
							LOGGER.warning(String.format("Subscriber error receiving %s, discarding frame: %s", topic, e.getMessage()));
							transport.discardFrame();
						}
					}
				}
			}, "subscription").start();

			return sub;
		}

		private Event recvEventCreated(String op, FProtocol iprot) throws TException {
			TMessage msg = iprot.readMessageBegin();
			if (!msg.name.equals(op)) {
				TProtocolUtil.skip(iprot, TType.STRUCT);
				iprot.readMessageEnd();
				throw new TApplicationException(TApplicationException.UNKNOWN_METHOD);
			}
			Event req = new Event();
			req.read(iprot);
			iprot.readMessageEnd();
			return req;
		}

	}

}