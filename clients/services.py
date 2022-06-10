
import csv
import os
from clients.models import Client

class ClientService:
    def __init__ (self, table_name:str):
        self.table_name = table_name

    def create_client (self, client:Client) -> None:
        with open(self.table_name, mode="a") as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients (self) -> tuple[dict, ...]:
        with open(self.table_name, mode="r") as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            
            return tuple(reader)

    def update_clients (self, client_updated:Client) -> None:
        client_list = self.list_clients()

        updated_clients = []
        for client in client_list:
            if client["idx"] == client_updated.idx:
                updated_clients.append(client_updated.to_dict())
            else:
                updated_clients.append(client)

        if client_list == updated_clients:
            return # No changes in Clients db, skip rewrite

        self._save_to_disk(tuple(updated_clients))

    def delete_clients (self, client_deleted:Client) -> None | Client:
        client_list = self.list_clients()

        updated_clients = []
        for client in client_list:
            if client["idx"] != client_deleted.idx:
                updated_clients.append(client)

        if client_list == updated_clients:
            # No Changes in Clients db, skip rewrite
            return None
    
        self._save_to_disk(tuple(updated_clients))
        return client_deleted

    def _save_to_disk (self, client_list:tuple[dict, ...]) -> None:
        temporal_table_name = self.table_name + ".tmp"
        with open(temporal_table_name, mode="w+") as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(client_list)
        
        os.remove(self.table_name)
        os.rename(temporal_table_name, self.table_name)
