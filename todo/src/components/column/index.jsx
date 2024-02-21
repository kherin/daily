import React from "react";

export default function Column(props) {
  return (
    <div>
      <h1>{props.name}</h1>
      <div>
        <span>
          {props.items

            .filter(({ state }) => state == props.name)
            .map(({ title }) => (
              <p key={title}>{title}</p>
            ))}
        </span>
      </div>
    </div>
  );
}
