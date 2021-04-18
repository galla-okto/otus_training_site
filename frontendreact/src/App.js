import './App.css';
import React from "react";
import LoginForm from "./components/auth";
import Header from "./components/header";
import WorkoutsList from "./components/workouts-list";
import WorkoutsCard from "./components/workouts-card";
import WorkoutsCardEnroll from "./components/workouts-card-enroll";
import PersonalArea from "./components/personal-area";


class App extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      'workouts': [

      ],
      isAuth: false
    }
  }

  auth(login, password) {
    console.log(login)
    console.log(password)
    this.setState({isAuth: true})
  }

  render() {
    return (
      <div className="App">
        <Header />
        {this.state.isAuth
            ? <button>Logout</button>
            : <LoginForm auth={(login, password) => this.auth(login, password)} />}
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
      </div>
    );
  }
}

export default App
