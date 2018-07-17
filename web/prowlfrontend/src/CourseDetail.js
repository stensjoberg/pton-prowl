import React, { Component } from 'react'
import Radium from 'radium'
import { getCourse } from './helper'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class CourseDetail extends Component {

  state = {
    course: {}
  }

  async componentDidMount() {
    const id = this.props.match.params.courseId
    const course = await getCourse({id: id})
    this.setState({
      course
    })
  }

  async componentDidUpdate(prevProps) {
    if ((prevProps.match.params.courseId === undefined && this.props.match.params.courseId !== undefined) ||
        (prevProps.match.params.courseId !== this.props.match.params.courseId)) {
      const id = this.props.match.params.courseId
      const course = await getCourse({id: id})
      this.setState({
        course
      })
    }
  }

  render() {
    const course = this.state.course
    if (course.codes === undefined) {
      return false
    }
    else {
      console.log(course)
      return (
        <div className="flexcontainer vert">
          <h1>{course.title}</h1>
          <ul>
          {course.codes.map((code) => (
            <li key={code.id}>{code.id}</li>
          ))}
          </ul>

        </div>
      );
    }
  }
}

export default Radium(CourseDetail)
