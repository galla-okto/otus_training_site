import React from "react";
import App from "../../../frontend/src/components/App";

class WorkoutList extends React.Component {
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

                  {workout.name} - *({workout.star_rating})*


              </li>
          );
          })}
      </ul>
    );
  }
}

export default WorkoutList;