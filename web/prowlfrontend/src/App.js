// App.js
import React, { Component } from 'react'
import Radium from 'radium'
import CourseBoxList from './CourseBoxList'
import { styles } from './styles'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';




class App extends Component {
  render() {
    return (
      <div class="flexcontainer hor">
        <CourseBoxList/>
      </div>
    );
  }
}

export default Radium(App);
