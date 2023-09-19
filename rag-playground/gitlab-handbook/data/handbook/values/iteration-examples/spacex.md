---
title: "Iteration at SpaceX"
description: Learn more about how SpaceX and Elon Musk iterate
canonical_path: "/handbook/values/iteration-examples/spacex/"
---

## Iteration at SpaceX

SpaceX has been one of the few private companies who have been able to break into the space launch business, with a number of firsts ([full list](https://en.wikipedia.org/wiki/SpaceX#Summary_of_achievements)):

- First private company to successfully launch, orbit, and recover a spacecraft.
- First private company to send a human-rated spacecraft to orbit.
- First reuse, reflight and landing of an orbital first stage.
- Largest commercial satellite constellation operator in the world.

While there are likely many reasons for their success, Elon Musk highlighted in [an interview with Tim Dodd](https://www.youtube.com/watch?v=t705r8ICkRw) their process for building new features and products. It is composed of five steps:

1. Challenge and refine requirements
1. Try to remove part/process
1. Simplify and optimize
1. Accelerate cycle time
1. Automate

It is worth going into each of these in more detail, and how they can relate to GitLab.

### Challenge and refine requirements

Elon says in the interview:

> Your requirements are definitely dumb. It does not matter who gave them to you. It’s particularly dangerous if a smart person gave you the requirements because you might not question them enough.
>
> ...
>
> Everyone’s wrong, no matter who you are, everyone’s wrong some of the time. Also, whatever requirement or constraint you have it must come with a name, not a department. Because you can’t ask the department, you have to ask a person. And that person who’s pulling for the requirement or constraint must agree that they must take responsibility for that requirement.

For GitLab, one can translate this into two key actions:

1. Ensure we have a strong understanding of the problem we want to solve
1. Ensure there is well-documented and compelling justifications for each requirement in the epics and issues for the given change

These two actions help to ensure our requirements are "less dumb" and it is clear to all why a given requirement is in place.

### Try to remove part/process

Elon says in the interview:

> The bias tends to be very strongly towards lets’s add this part of the process in case we need it, but you can basically make “in case” arguments for so many things.
>
> ...
>
> This is actually very important. If you’re not occasionally adding things back in, you are not deleting enough.

This is indeed important, especially as a company and a product scale and grow over time. As noted by Elon, there is a natural inclination to add a process or feature for every single scenario. This however leads to very sub-optimal outcomes.

From a process standpoint, decision velocity can be slowed as well as overall time to market. From a product standpoint, the UX, code, and feature set can become so complex that it is difficult to learn, maintain, and use.

As you are building new features or introducing new code/processes, ask whether this is really needed, as well as whether by virtue of this addition could we deprecate existing features/code/processes.

### Simplify and optimize

> Then only in the third step is “Simplify or optimize”. The third step, not the first step. The reason it’s at the third step is because it’s very common, as possibly the most common error of a smart engineer is to optimize a thing that should not exist

For GitLab and software companies, one can translate this into a few recommended actions:

1. Challenge yourself on whether a given setting or feature is required. Is there a possibility to utilize [convention over configuration](https://about.gitlab.com/handbook/product/product-principles/#convention-over-configuration)? Each setting/feature generates an on-going maintenance cost, as well as cognitive load on users.
1. If you believe a feature is needed, ask yourself if there is a more general purpose way of solving this. Is there a small building block feature which could enable users to solve this problem, but also unlock the possibility to solve others? Could another feature be re-used or extended? An example of this is GitLab CI, where we provide a set of building blocks which users can assemble in many ways to solve a wide variety of problems, as well as incident management which re-uses issues.

[Convention over Configuration](https://about.gitlab.com/handbook/product/product-principles/#convention-over-configuration)

### Accelerate cycle time

Elon notes in the interview:

> You’re moving too slowly, go faster. But don’t go faster until you work on the other three things first.
>
> If you’re digging, you know, your grave, don’t dig it faster. Stop digging your grave, you know.

This principle aligns well with a few of GitLab's core values, such as:

- [Iteration](/handbook/values/#iteration)
- [Velocity over predictabitlity](https://about.gitlab.com/handbook/engineering/development/principles/#velocity-over-predictability)

### Automate

Once a feature or process finds product fit or is validated to be of significant positive value, it should be a candidate for further automation. This is particularly important to do last, since spending the time up front to automate a un-validated solution to a problem is particularly risky and not very iterative.

While this may seem to be common sense as part of this flow, it is often times counter-intertuitive in practice. This is because there is a strong desire to reduce manual touches, or to launch with a great UX from the very beginning. The challenge is that this often significantly increases the iteration size, and can delay important learnings which may cause a change in direction.

As Elon notes in the interview:

> The final step is “Automate”. Now, I have personally made the mistake of going backwards on all five steps multiple times. So I have to repeat this - yes, multiple times.
