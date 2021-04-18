import './App.css';
import React from "react";
import LoginForm from "./components/auth";
import Header from "./components/header";
import WorkoutsList from "./components/workouts-list";
import WorkoutsCard from "./components/workouts-card";
import WorkoutsCardEnroll from "./components/workouts-card-enroll";
import PersonalArea from "./components/personal-area";
import axios from "axios";

class App extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
        isAuth: false,
        token: ''
    }
  }

  logout() {
    this.setState({isAuth: false, token: ''})
  }

  auth(login, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: login, password: password})
    .then(response => {
        const token = response.data['token']
        this.setState({token: token})
        this.setState({isAuth: true})
    }).catch(error => alert('Неверный логин или пароль'))

    // console.log(login)
    // console.log(password)
    // this.setState({isAuth: true})
  }

  render() {
    return (
      <div className="App">
        <Header />
        {this.state.isAuth
            ? <button onClick={() => this.logout()}>Logout</button>
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
        {/*<PersonalArea token={this.state.token} />*/}
      </div>
    );
  }
}

export default App
