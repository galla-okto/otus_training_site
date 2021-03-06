import React from "react";
import Header from "./header";
import WorkoutsList from "./workouts-list";
import WorkoutsCard from "./workouts-card";
import WorkoutsCardEnroll from "./workouts-card-enroll";
import PersonalArea from "./personal-area";
import LoginForm from "./auth";


class Main extends React.Component {
  render() {
    return (
        <div>
            <Header />
            <WorkoutsList />
            <br />
            <br />
            <h3>Страница просмотра одного курса</h3>
            <WorkoutsCard code={"1"}/>
            <br />
            <br />
            <h3>Страница с возможностью записи на курс</h3>
            <WorkoutsCardEnroll />
            <PersonalArea />
            <LoginForm />
        </div>
    );
  }
}

export default Main;