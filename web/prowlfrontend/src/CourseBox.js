import React, { Component } from 'react'
import Radium from 'radium'
import Button from './Button'
import { styles } from './styles'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class CourseBox extends Component {
  render() {
    return (
      <div class="flexcontainer hor coursebox">

        <p>{this.props.title}</p>
        <Button>+</Button>
      </div>
    );
  }
}

export default Radium(CourseBox)
