import React from "react";
import Button from 'react-bootstrap/Button';
import Header from "./header";


class Main extends React.Component {
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
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
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
            <Header />
          <ul>
              {this.state.data.map(workout => {
              return (
                  <li key={workout.id}>
                      {workout.name} - *({workout.star_rating})*
                  </li>
              );
              })}
          </ul>

          <Button onClick={() => alert('hey')}>Show Toast</Button>
        </div>
    );
  }
}

export default Main;