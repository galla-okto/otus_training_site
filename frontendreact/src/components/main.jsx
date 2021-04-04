import React from "react";
import Header from "./header";
import WorkoutsList from "./workouts-list";


class Main extends React.Component {
  render() {
    return (
        <div>
            <Header />
            <WorkoutsList />
        </div>
    );
  }
}

export default Main;