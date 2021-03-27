import { render } from "react-dom";
import React, { Component } from "react";


class Card extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }

    componentDidMount() {
        const url_card = "http://127.0.0.1:8000/myapi/api/workouts/1";
        fetch(url_card)
          .then(response => {
            if (response.status > 400) {
              return this.setState(() => {
                return { placeholder: "Something went wrong!" };
              });
            }
            return response.json();
          })
          .then(data => {
            this.setState(() => {
              return {
                data,
                loaded: true
              };
            });
          });
    }

    render() {
        return (
            <div>
                <h3>{ this.state.data.name }</h3>
                <p>{ this.state.data.description }</p>
            </div>
        )
    }
}

export default Card;

const container2 = document.getElementById("card");
render(<Card />, container2);
