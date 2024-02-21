import React, { useEffect, useState } from "react";

// api
import ItemService from "../../api/items";

// styling
import "./styles.css";

// componenst
import Column from "../column";

export default function Board() {
  const [columns, setColumns] = useState([
    {
      columnName: "Todo",
    },
    {
      columnName: "Done",
    },
    {
      columnName: "Backlog",
    },
    {
      columnName: "Doing",
    },
  ]);

  const [items, setItems] = useState([]);

  useEffect(() => {
    ItemService.fetchItems().then((data) => {
      setItems(data);
    });
  }, []);

  return (
    <>
      <h1>Boards</h1>
      <div className="container">
        {columns.map(({ columnName }) => (
          <div key={columnName}>
            <Column key={columnName} name={columnName} items={items} />
          </div>
        ))}
      </div>
    </>
  );
}
