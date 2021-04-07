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
        const {code} = this.props;
        const url_workouts = "http://127.0.0.1:8000/myapi/api/workouts/"+code;

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
        const {data} = this.state;

        return (
        <div>
            <h2 className="panel-title">{data.name} {data.star_rating}*</h2>
            <p>Initial leve: {data.initial_level}</p>
            <p>{data.description}</p>
            <Button variant="secondary">Enroll in</Button>
        </div>
    );
  }
}

export default WorkoutsCard;