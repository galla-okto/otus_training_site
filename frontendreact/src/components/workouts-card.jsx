import React from "react";
import Button from "react-bootstrap/Button";

class WorkoutsCard extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    const url_workouts = "http://127.0.0.1:8000/myapi/api/workouts/1";
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
        let workout = this.state.data;

        return (
        <div>
            <h2 className="panel-title">{workout.name} {workout.star_rating}*</h2>
            <p>Initial leve: {workout.initial_level}</p>
            <p>{workout.description}</p>
            <Button variant="secondary">Enroll in</Button>
        </div>
    );
  }
}

export default WorkoutsCard;