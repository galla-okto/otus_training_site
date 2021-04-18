import React from "react";
import CardDeck from "react-bootstrap/CardDeck";
import Card from "react-bootstrap/Card";

class PersonalArea extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    const url_workouts = "http://127.0.0.1:8000/myapi/api/enrollments/";
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
            <h2 className="panel-title">Мои курсы</h2>
            <CardDeck>
                {this.state.data.map(workout => {
                    return (
                        <Card key={workout.id}>
                            <Card.Img variant="top" src="holder.js/100px160" />
                            <Card.Body>
                                <Card.Title>{workout.name} {workout.star_rating}*</Card.Title>
                                <Card.Text>
                                    {workout.description}
                                </Card.Text>
                                <Card.Link href="#">More</Card.Link>
                            </Card.Body>
                            <Card.Footer>
                                <small className="text-muted">Initial leve: {workout.initial_level}</small>
                            </Card.Footer>
                        </Card>
                    );
                })}
            </CardDeck>
        </div>
    );
  }
}

export default PersonalArea;
