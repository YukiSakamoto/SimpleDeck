from simple_deck import Client
import uuid

def main():
    client = Client("127.0.0.1", 50052, insecure = True)
    for feature_identifier in client.SiLAService.ImplementedFeatures.get():
        print("-- {}".format(feature_identifier))
    random_uuid = uuid.uuid4()
    print(random_uuid)
    a = client.SimpleDeckServer.PutItem("A", str(random_uuid), "tube")
    print(a)
    b = client.SimpleDeckServer.MoveItem("A", "B")
    print(b)
    c  = client.SimpleDeckServer.DeleteItem("B")
    print(c)

    client.SimpleDeckServer.NewConsumable('Water', 100)
    status = client.SimpleDeckServer.ConsumableState.get()
    print(status)
    refill_instance = client.SimpleDeckServer.Refill('Water', 20)
    #intermediate_refill_subscription = refill_instance.subscribe_to_intermediate_responses()
    import time
    while not refill_instance.done:
        print("Refilling: Progress: {}".format(refill_instance.progress))
        time.sleep(0.5)
    status = client.SimpleDeckServer.ConsumableState.get()
    print(status)

    refill_instance = client.SimpleDeckServer.Refill('Water', 120)
    while not refill_instance.done:
        print("Refilling: Progress: {}".format(refill_instance.progress))
        time.sleep(0.5)
    status = client.SimpleDeckServer.ConsumableState.get()
    print(status)



if __name__ == '__main__':
    main()