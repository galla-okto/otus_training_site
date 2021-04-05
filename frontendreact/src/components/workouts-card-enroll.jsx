import React from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";


class WorkoutsCardEnroll extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            workout: 'N/A',
            schedule: 'N/A',
            client: 'N/A',
            loaded: false,
            placeholder: "Loading"
        };
    }
    handleWorkout = (e) => this.setState({ workout: e.target.value})
    handleSchedule = (e) => this.setState({ schedule: e.target.value})

    render() {
        const { workout, schedule, client } = this.state;

        return (
            <Form.Group>
                <Form.Control size="lg" type="text" placeholder="Workout"
                              value={workout} onChange={this.handleWorkout}/>
                <br />
                <Form.Control type="text" placeholder="Schedule"
                              value={schedule} onChange={this.handleSchedule}/>
                <br />
                <Form.Control size="sm" type="text" placeholder="Client" readOnly value={client}/>

                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form.Group>
        );
    }
}

export default WorkoutsCardEnroll;
