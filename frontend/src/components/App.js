import { render } from "react-dom";
import React, { Component } from "react";


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    const url_workouts = "http://127.0.0.1:8000/myapi/api/workouts/";
    fetch(url_workouts)
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
      <ul>
          {this.state.data.map(workout => {
          return (
              <li key={workout.id}>
                <a href="{% url 'main:workout' pk=workout.pk %}">
                  {workout.name} - *({workout.star_rating})*
                </a>
                <a href="{% url 'main:workout-update' pk=workout.pk %}">Редактировать</a>
                <a href="{% url 'main:workout-delete' pk=workout.pk %}">Удалить</a>
              </li>
          );
        })}
      </ul>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);