from fastapi import APIRouter


class BaseRouter(APIRouter):
    def __init__(self, request_schema, response_schema, model):
        super().__init__()
        self.request_schema = request_schema
        self.response_schema = response_schema
        self.model = model

    def load_crud_routes(self):
        request_schema = self.request_schema
        response_schema = self.response_schema
        model = self.model

        @self.get("/", response_model=list[response_schema])
        async def fetch_all():
            return await response_schema.from_queryset(model.all())

        @self.get("/{item_id}", response_model=response_schema)
        async def fetch_one(item_id: str):
            return await response_schema \
                .from_queryset_single(model.get(id=item_id))

        @self.post("/", status_code=201, response_model=response_schema)
        async def create(item: request_schema):
            new_item = await model.create_one(item)
            return await response_schema.from_tortoise_orm(new_item)

        @self.put("/{item_id}", response_model=response_schema)
        async def update(item_id: str, item: request_schema):
            print(item.dict())
            updated_item = await model.update_one(item_id, item)
            return await response_schema.from_queryset_single(updated_item)

        @self.delete("/{item_id}")
        async def delete(item_id: str):
            await model.delete_one(item_id)
            return {"message": "Item deleted successfully"}

