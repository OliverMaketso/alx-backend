import kue from 'kue'

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
];

const queue = kue.createQueue({name: 'push_notification_code_2'});

for (const job of jobs) {
    const jobNotification= queue.create('push_notification_code_2', job)

    jobNotification
        .on('enqueue', () => {
            console.log('Notification job created:', jobNotification.id);
        })
        .on('complete', () => {
            console.log('Notification job', jobNotification.id, 'completed');
        })
        .on('failed', (err) => {
            console.log('Notification job', jobNotification.id, 'failed:', err.message || err.toString());
        })
        .on('progress', (progress, _data) => {
            console.log('Notification job', jobNotification.id, `${progress}% complete`);
          });
        jobNotification.save();
}
