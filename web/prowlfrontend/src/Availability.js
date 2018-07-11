import React, { Component } from 'react'
import Radium from 'radium'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class CourseDetail extends Component {

  state = {
    availability: this.props.data
  };

  handleSumbit = async (event) => {
    return true
  }

  render() {
    if (this.state.availability === undefined) {
      return false
    }
    else {
      console.log("Availability: ")
      console.log(this.state.availability)
      return (
        <h1>available</h1>
      )
    }
  }
}

export default Radium(CourseDetail)
