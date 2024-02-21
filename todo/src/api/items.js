const fetchItems = () => {
  return fetch("<<ITEMS ENDPOINT>>").then((response) => response.json());
};

const ItemService = {
  fetchItems,
};

export default ItemService;
