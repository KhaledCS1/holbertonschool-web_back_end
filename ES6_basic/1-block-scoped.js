export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // These constants are block-scoped and do not affect the outer variables
    const task = true;
    const task2 = false;
    console.log(task, task2); // Optional: visible only inside this block
  }

  // Return the outer-scope constants
  return [task, task2];
}