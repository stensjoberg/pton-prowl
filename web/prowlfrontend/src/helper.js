export default async function getCourse(id) {
  try {
    const res = await fetch('http://0.0.0.0:8000/api/v1/courses/' + id, {
          headers: {
          'Authorization': 'Token ' + localStorage.getItem('token'),
        }
      }
    )
    const course = await res.json()
    return course
  } catch (e) {
    console.log(e)
  }
}
