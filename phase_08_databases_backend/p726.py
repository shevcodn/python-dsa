import redis.asyncio as redis
import asyncio

redis_client = redis.from_url("redis://localhost:6379/0")

async def subscriber():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("notifications")
    listen = pubsub.listen()
    await asyncio.sleep(5)
    print("Subscribed to 'notifications' channel. Waiting for messages...")
    async for message in listen:
        if message["type"] == "message":
            print(f"Received message: {message['data'].decode()}")
            await redis_client.publish("notifications", message["data"])
            await asyncio.sleep(5)

async def publisher():
    count = 1
    while True:
        message = f"Notification {count}"
        await redis_client.publish("notifications", message)
        print(f"Published: {message}")
        count += 1
        await asyncio.sleep(5)
        message = f"Alert {count}"
        await redis_client.publish("notifications", message)
        print(f"Published: {message}")
        count += 1
        await asyncio.sleep(5)
        print("Publishing a burst of messages...")
        for i in range(5):
            burst_message = f"Burst {i + 1}"
            await redis_client.publish("notifications", burst_message)
            print(f"Published: {burst_message}")
        await asyncio.sleep(5)

async def main():
    await asyncio.gather(subscriber(), publisher())

if __name__ == "__main__":
    asyncio.run(main())