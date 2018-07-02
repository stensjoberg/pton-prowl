// App.js
import React, { Component } from 'react'
import Radium from 'radium'
import CourseBoxList from './CourseBoxList'
import Whenisgood from './Whenisgood'
import LoginForm from './LoginForm'
import { styles } from './styles'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';




class App extends Component {
  render() {
    return (
      <div className="flexcontainer hor">
        <CourseBoxList/>
        <Whenisgood/>
        <LoginForm/>
      </div>
    );
  }
}

export default Radium(App);
