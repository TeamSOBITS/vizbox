cmake_minimum_required(VERSION 3.10.2)
project(vizbox)

find_package(catkin REQUIRED COMPONENTS
	message_generation
)

add_message_files(
  DIRECTORY msg
  FILES
  Story.msg
)
generate_messages(
  DEPENDENCIES
)

catkin_package(
  CATKIN_DEPENDS
  message_runtime
)