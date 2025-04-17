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


if __name__ == '__main__':
    main()